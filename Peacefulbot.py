import socket
import json


class PeacefulBot:
    def __init__(self):

        # Load all commands on startup
        with open('commands.json', 'r') as f:
            commands = f.read()

        self.commands = json.loads(commands)

        self.commands_dict = {}

        for (k, v) in self.commands.items():
            # Create bools for toggle-commands
            if v["type"] == "toggle":
                self.commands_dict.update({k: False})

        # Get Settings from settings.json
        with open('settings.json', 'r') as f:
            settings = f.read()

        settings = json.loads(settings)

        self.CHANNEL = settings["channel"]
        self.MODLIST = settings["mods"]

        self.s = socket.socket()
        self.s.connect((settings["host"], settings["port"]))

        self.s.send((f"PASS " + settings["pass"] + "\r\n").encode('utf-8'))
        self.s.send((f"NICK " + settings["nick"] + "\r\n").encode('utf-8'))
        self.s.send((f"JOIN #" + settings["channel"] + "\r\n").encode('utf-8'))

        readbuffer = ""
        loading = True

        while loading:
            readbuffer += self.s.recv(2048).decode('utf-8')
            temp = readbuffer.split("\n")
            readbuffer = temp.pop()

            for line in temp:
                print(line)
                if ("End of /NAMES list" in line):
                    loading = False
                else:
                    loading = True

        # Confirming connection
        self.sendMessage("PeacefulBot is connected!")

    def sendMessage(self, message):
        messageTemp = f"PRIVMSG #" + self.CHANNEL + " :" + message
        self.s.send((messageTemp + "\r\n").encode('utf-8'))
        print("Sent: " + messageTemp)

    def getUser(self, line):
        return (line.split(":", 2)[1].split("!", 1)[0])

    def getMessage(self, line):
        return (line.split(":", 2)[2])

    def listenToChat(self):
        readbuffer = self.s.recv(2048).decode('utf-8')
        temp = readbuffer.split("\n")

        for line in temp:
            # Ping back to keep connection
            if "PING" in line:
                # send msg to the server, not to chat. This is different from sendMessage custom definition
                self.s.send(
                    bytes((line.replace("PING", "PONG")+"\n").encode('utf-8'))
                )
                print("I just sent a PONG")
                return ({
                    "user": "Twitch",
                    "msg": line
                })
            else:
                return ({
                    "user": self.getUser(line),
                    "msg": self.getMessage(line)
                })

    def run(self):
        # Mainloop for the bot
        while True:
            line = self.listenToChat()
            print(line)

            # Check for commands from commands.json
            for (k, v) in self.commands.items():
                if k in line["msg"]:
                    if (v["permission"] == "mods" and line["user"] in self.MODLIST) or v["permission"] == "everyone":
                        if v["type"] == "toggle":
                            self.commands_dict[k] = not self.commands_dict[k]
                            if self.commands[k]:
                                self.sendMessage(
                                    v["true_message"].format(**line)
                                )
                            else:
                                self.sendMessage(
                                    v["false_message"].format(**line)
                                )
                        elif v["type"] == "message":
                            self.sendMessage(
                                v["message"].format(**line)
                            )
                        else:
                            print("Unknown command type " + v["type"] + "!")

            # Check for info command
            if "!info" in line["msg"]:
                for value in self.commands_dict:
                    self.sendMessage(
                        value.replace("!", "") + ": " +
                        str(self.commands_dict[value]).replace(
                            "True", "Yes").replace("False", "No")
                    )
