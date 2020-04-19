import socket
import string
from Settings import HOST, PORT, PASS, NICK, CHANNEL


class PeacefulBot:
    def __init__(self, HOST, PORT, PASS, NICK, CHANNEL):
        self.HOST = HOST
        self.PORT = PORT
        self.PASS = PASS
        self.NICK = NICK
        self.CHANNEL = CHANNEL

    def openSocket(self):
        self.s = socket.socket()
        self.s.connect((self.HOST, self.PORT))

        self.s.send((f"PASS " + self.PASS + "\r\n").encode('utf-8'))
        self.s.send((f"NICK " + self.NICK + "\r\n").encode('utf-8'))
        self.s.send((f"JOIN #" + self.CHANNEL + "\r\n").encode('utf-8'))

    def joinRoom(self):
        readbuffer = ""
        loading = True

        while loading:
            readbuffer += self.s.recv(2048).decode('utf-8')
            temp = readbuffer.split("\n")
            readbuffer = temp.pop()

            for line in temp:
                print(line)
                loading = self.loadingComplete(line)

        self.sendMessage("PeacefulBot is connected!")

    def loadingComplete(self, line):
        if ("End of /NAMES list" in line):
            return False
        else:
            return True

    def sendMessage(self, message):
        messageTemp = f"PRIVMSG #" + self.CHANNEL + " :" + message
        self.s.send((messageTemp + "\r\n").encode('utf-8'))
        print("Sent: " + messageTemp)


# Connect to Twitch
bot = PeacefulBot(HOST, PORT, PASS, NICK, CHANNEL)
bot.openSocket()
bot.joinRoom()

while True:
    persist = True
