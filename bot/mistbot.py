#################
#  MistBot - Chat Bot
#  Version: 1.5
#  Author: Tim Monfette (Timmiluvs)
#  Date: 02/17/2017
##################

# bot.py
# Bot functionality

import config
import commands
import socket
import time
import re

# Connect to Twitch IRC
s = socket.socket()
s.connect((config.HOST, config.PORT))
s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(config.NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(config.CHAN).encode("utf-8"))
s.send("CAP REQ :twitch.tv/tags\r\n".encode("utf-8"))

# Proccess all incoming messages
while True:
    response = s.recv(1024).decode("utf-8") 
    if response == "PING :tmi.twitch.tv\r\n":       # Twitch checking if we are alive
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))   # Yes, we are alive
    else:
        fields = re.split(';', response)
        modCheck = fields[0]
        lastField = re.split(':', fields[len(fields)-1])
        message = lastField[len(lastField)-1]
        if (("broadcaster" in modCheck) or ("moderator" in modCheck)):
            for pattern in config.PATT:
                if re.match(pattern, message):
                    com = message.strip("!").strip().lower()
                    getattr(commands, com)(s)
                    break
    time.sleep(1.5)
