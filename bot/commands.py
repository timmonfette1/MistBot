#################
#  PlayET - Chat Bot
#  Version: 0.5
#  Author: Tim Monfette (Timmiluvs)
##################

# commands.py
# Commands bot recognizes

import config

# Send a chat message
def chat(sock, message):
    sock.send('PRIVMSG %s :%s\n' % (config.CHAN, message.encode('utf-8')))

# Twitter funciton
def twitter(sock):
    msg = "You can follow me on Twitter at https://twitter.com/timmiluvs"
    chat(sock, msg)
