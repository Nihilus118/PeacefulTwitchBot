from Peacefulbot import PeacefulBot
from Settings import HOST, PORT, PASS, NICK, CHANNEL

# Connect to Twitch
bot = PeacefulBot(HOST, PORT, PASS, NICK, CHANNEL)

modList = [
    "peacefulstorm13",
    "nihilusstream",
    "mrpanda2k"
]

noreset = False
xdskip = False
apgf = False
darkside = False

while True:
    line = bot.listenToChat()
    print(line)

    if "!resetAll" in line["msg"] and line["user"] in modList:
        noreset = False
        xdskip = False
        apgf = False
        darkside = False

    if "!noreset" in line["msg"] and line["user"] in modList:
        noreset = not noreset
        if noreset:
            bot.sendMessage("This is now a noreset run!")
        else:
            bot.sendMessage("This is a not a noreset run!")

    if "!xdskip" in line["msg"] and line["user"] in modList:
        xdskip = not xdskip
        if xdskip:
            bot.sendMessage("This is now a xdskip run!")
        else:
            bot.sendMessage("This is a not a xdskip run!")

    if "!apgf" in line["msg"] and line["user"] in modList:
        apgf = not apgf
        if apgf:
            bot.sendMessage("This is now a apgf run!")
        else:
            bot.sendMessage("This is a not a apgf run!")

    if "!darkside" in line["msg"] and line["user"] in modList:
        darkside = not darkside
        if darkside:
            bot.sendMessage("This is now a darkside run!")
        else:
            bot.sendMessage("This is a not a darkside run!")

    if "!info" in line["msg"]:
        if noreset:
            bot.sendMessage("This is a noreset run!")
        else:
            bot.sendMessage("This is not a noreset run!")
        if xdskip:
            bot.sendMessage("This is a xdskip run!")
        else:
            bot.sendMessage("This is not a xdskip run!")
        if apgf:
            bot.sendMessage("This is an apgf run!")
        else:
            bot.sendMessage("This is not an apgf run!")
        if darkside:
            bot.sendMessage("This is a darkside run!")
        else:
            bot.sendMessage("This is not a darkside run!")
