#################
#  MistBot - Chat Bot
#  Version: 1.1
#  Author: Tim Monfette (Timmiluvs)
#  Date: 01/27/2017
##################

# commands.py
# Commands bot recognizes

import config

# Send a chat message
def chat(sock, message):
    sock.send('PRIVMSG %s :%s\n' % (config.CHAN, message.encode('utf-8')))

# Twitter funciton
def twitter(sock):
    msg = "You can follow my Twitter for updates on when I'll be live as well as other thoughts in my head! https://twitter.com/mist_master1"
    chat(sock, msg)

# Youtube function
def youtube(sock):
    msg = "I'm also on YouTube, you can find various videos and Lets Plays on there! https://www.youtube.com/channel/UCuE7BgKOUd-CO6RgSLlYY0Q"
    chat(sock, msg)

# Hype function
def hype(sock):
    msg = "╲⎝⧹╲⎝⧹ PogChamp ⧸⎠╱⧸╱"
    chat(sock, msg)

# New 1.5 All Worlds Route function
def route(sock):
    msg = "The new route can be found here http://pastebin.com/2qc347zY"
    chat(sock, msg)