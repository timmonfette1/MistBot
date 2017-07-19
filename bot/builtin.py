#################
#  PlayET - Chat Bot
#  Version: 0.5
#  Author: Tim Monfette (Timmiluvs)
##################

# builtins.py
# Built in commands/functions

import csv
from ast import literal_eval

import config

# Save the command list
def saveCL():
    with open('cl.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in config.CL.items():
            writer.writerow([key, value])

# Build the command list
def buildCL():
    commandList = {}
    with open('cl.csv', 'rb') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            commandList[row[0]] = literal_eval(row[1])

        return commandList

# Add a command
# HOW TO CALL:
#   newCom = "!addcom testing all Test command"
#   split = newCom.split(" ")
#   builtin.addCommand(' '.join(split[1:]))
def addCommand(message):
    split = message.split(" ")

    if split[0] in config.CL:
        print "Command \"" + split[0] + "\" already exists. Please delete it then re-add it if you wish to edit it."
        return
    else:
        config.CL[split[0]] = (split[1], " ".join(split[2:]))

# Delete a command
def delCommand(command):
    if command in config.CL:
        del config.CL[command]
    else:
        print "Command \"" + command + "\" doesn't exist. Cannot delete."
