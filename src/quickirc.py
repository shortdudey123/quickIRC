#!/usr/bin/python
import socket


class quickIRC:

    def __init__(self, server, port=6667, nick="quickIRC"):
        self.server = server
        self.port = port
        self.nick = nick
        self.channels = {}
        self.debug = False

        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.irc.connect((self.network,self.port))
        data = self.irc.recv (4096)
        print data
        self.irc.send("USER "+ self.nick +" "+ self.nick +" "+ self.nick +" :quickIRC message bot\n")
        self.irc.send("NICK "+ self.nick +"\n")
        return

    def disconnect():
        self.irc.send('QUIT\n')
        self.irc.close()
        return

    def sendMessage(self, message, channels=''):
        # connect to the irc server
        connect()

        # JOIN, PRIVMSG, PART
        for channel in self.channels:
            irc.send("JOIN "+ channel + self.channels[channels] + "\n")
            irc.send("PRIVMSG "+ channel + " : " + message + "\n")
            irc.send("PART "+ channel + "\n")

        # close the server connection
        disconnect()
        return

    def setDefaultChannels(self, channels):
        if type(channels) = dict:
            self.channels = channels
        elif type(channels) = list:
            for channel in channels:
                self.channels[channel] = ''
        elif type(channels) = str:
            self.channels[channels] = ''
        return

    def setChannelKey(self, channel, key):
        self.channels[channel] = key
        return

    def setDebug(self, debug):
        self.debug = debug