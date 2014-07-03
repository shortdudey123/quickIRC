#!/usr/bin/python
import socket


class quickIRC:

    def __init__(self, server, port=6667, nick="quickIRC"):
        self.server = server
        self.port = port
        self.nick = nick
        self.channels = {}

        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.irc.connect((self.network,self.port))
        data = self.irc.recv (4096)
        print data
        irc.send("USER "+ self.nick +" "+ self.nick +" "+ self.nick +" :quickIRC message bot\n")
        irc.send("NICK "+ self.nick +"\n")

    def disconnect():
        irc.send ('QUIT\r\n')

    def sendMessage(self, message, channels=''):
        connect()

        disconnect()

    def setDefaultChannels(self, channels):
        if type(channels) = 