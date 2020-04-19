from Peacefulbot import PeacefulBot
import json

# Get Settings from settings.json
with open('settings.json', 'r') as f:
    settings = f.read()

settings = json.loads(settings)

# Connect to Twitch
bot = PeacefulBot(
    settings["host"],
    settings["port"],
    settings["pass"],
    settings["nick"],
    settings["channel"]
)

modList = settings["mods"]

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

        bot.sendMessage("All values are now resetted.")

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
        msg = ""
        if noreset:
            msg += "This is a noreset run! "
        else:
            msg += "This is not a noreset run! "
        if xdskip:
            msg += "This is a xdskip run! "
        else:
            msg += "This is not a xdskip run! "
        if apgf:
            msg += "This is an apgf run! "
        else:
            msg += "This is not an apgf run! "
        if darkside:
            msg += "This is a darkside run!"
        else:
            msg += "This is not a darkside run!"

        bot.sendMessage(msg)
