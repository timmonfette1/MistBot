#################
#  MistBot - Chat Bot
#  Version: 1.1
#  Author: Tim Monfette (Timmiluvs)
#  Date: 01/27/2017
##################

# bot.py
# Bot functionality

import config
import commands
import socket
import time
import re

CHAT_MSG=re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

# Connect to Twitch IRC
s = socket.socket()
s.connect((config.HOST, config.PORT))
s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(config.NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(config.CHAN).encode("utf-8"))

# Proccess all incoming messages
while True:
    response = s.recv(1024).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":       # Twitch checking if we are alive
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))   # Yes, we are alive
    else:
        username = re.search(r"\w+", response).group(0) # saves username of person who sent message
        message = CHAT_MSG.sub("", response)    # their message
        for pattern in config.PATT:
            if re.match(pattern, message):
                com = message.strip("!").strip().lower()
                getattr(commands, com)(s)
                break
    time.sleep(1.5)
