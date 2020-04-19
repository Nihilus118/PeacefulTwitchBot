import socket


class PeacefulBot:
    def __init__(self, HOST, PORT, PASS, NICK, CHANNEL):
        self.CHANNEL = CHANNEL

        self.s = socket.socket()
        self.s.connect((HOST, PORT))

        self.s.send((f"PASS " + PASS + "\r\n").encode('utf-8'))
        self.s.send((f"NICK " + NICK + "\r\n").encode('utf-8'))
        self.s.send((f"JOIN #" + CHANNEL + "\r\n").encode('utf-8'))

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
                self.s.send((line.replace("PING", "PONG")).encode('utf-8'))
                print("PONG")
                return ({
                    "user": "Twitch",
                    "msg": line
                })
            else:
                return ({
                    "user": self.getUser(line),
                    "msg": self.getMessage(line)
                })
