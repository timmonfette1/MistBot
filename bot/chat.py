#################
#  PlayET - Chat Bot
#  Version: 0.5
#  Author: Tim Monfette (Timmiluvs)
##################

# chat.py
# Functions related to chatting

import config

# Send a chat message
def chat(sock, message):
    sock.send('PRIVMSG %s :%s\n' % (config.CHAN, message.encode('utf-8')))

# Execute a command
def executeCommand(sock, command):
    try:
        msg = config.CL[command][1]
        chat(sock, msg)
    except KeyError, e:
        None

# Check user permission for a command
def checkPermission(modCheck, command):
    try: 
        if (("broadcaster" in modCheck) or ("moderator" in modCheck)):
            return True
        else:
            comLevel = config.CL[command][0]
            if comLevel is not "all":
                return False
    except KeyError, e:
        None
