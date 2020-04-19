from Peacefulbot import PeacefulBot
from Settings import HOST, PORT, PASS, NICK, CHANNEL

# Connect to Twitch
bot = PeacefulBot(HOST, PORT, PASS, NICK, CHANNEL)
bot.openSocket()
bot.joinRoom()

while True:
    persist = True
