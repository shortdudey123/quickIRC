#!/usr/bin/env python
# =============================================================================
# file = quickirc.py
# description = Quickly and easily post messages to an IRC server
# author = GR <https://github.com/shortdudey123>
# create_date = 2014-07-02
# mod_date = 2014-07-03
# version = 0.1
# usage = called as a class
# notes =
# python_ver = 2.7.6
# =============================================================================

import socket
import time


class quickIRC(object):

    def __init__(self, server, port=6667, nick="quickIRC", identify='', debug=False, connectDelay=2):
        self.server = server
        self.port = port
        self.nick = nick
        self.channels = {}
        self.debug = debug
        self.identify = identify
        self.connectDelay = connectDelay

        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connectToServer(self):
        self.irc.connect((self.server, self.port))

        # need to wait for the server to respond
        time.sleep(self.connectDelay)

        if self.debug:
            print self.getData()
            print "~~~~~~~~~~~~~~"

        self.irc.send("USER " + self.nick + " " + self.nick + " " + self.nick + " :quickIRC message bot\n")
        self.irc.send("NICK " + self.nick + "\n")

        if self.identify != '':
            self.irc.send("PRIVMSG nickserv :identify {0} {1}\r\n".format(self.nick, self.identify))

        # need to wait for the server to respond
        time.sleep(self.connectDelay)

        if self.debug:
            print self.getData()
            print "~~~~~~~~~~~~~~"

        return

    def disconnectFromServer(self):
        self.irc.send('QUIT\n')
        self.irc.close()
        return

    def sendMessage(self, message, channels=''):
        if type(channels) == str:
            channels = [channels]

        # connect to the irc server
        self.connectToServer()

        all_channels = self.channels
        if channels != ['']:
            all_channels = all_channels + channels

        # JOIN, PRIVMSG, PART
        for channel in all_channels:

            if self.debug:
                print "*** Sending message in {0} ***".format(channel)

            self.irc.send("JOIN " + channel + self.channels[channel] + "\n")
            self.irc.send("PRIVMSG " + channel + " : " + message + "\n")
            self.irc.send("PART " + channel + "\n")

            if self.debug:
                print self.getData()
                print "~~~~~~~~~~~~~~"

        # close the server connection
        self.disconnectFromServer()
        return

    def setDefaultChannels(self, channels):
        if type(channels) == dict:
            self.channels = channels
        elif type(channels) == list:
            for channel in channels:
                self.channels[channel] = ''
        elif type(channels) == str:
            self.channels[channels] = ''
        return

    def setChannelKey(self, channel, key):
        self.channels[channel] = key
        return

    def setDebug(self, debug):
        self.debug = debug
        return

    def getData(self):
        # 16kb buffer allows for huge messages (i.e. MOTD)
        data = self.irc.recv(16384)
        return data
