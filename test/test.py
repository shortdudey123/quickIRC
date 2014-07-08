#!/usr/bin/env python
# =============================================================================
# file = test.py
# description = This will test the quickIRC class and its methods
# author = GR <https://github.com/shortdudey123>
# create_date = 2014-07-07
# mod_date = 2014-07-03
# version = 0.1
# usage = test for quickIRC class
# notes =
# python_ver = 2.6.6
# =============================================================================


import site
site.addsitedir("../src")

from quickirc import *

if __name__ == "__main__":
	q = quickIRC(server="chat.freenode.net", port=6667, nick="quickIRC", debug=True, connectDelay=4)
	q.setDefaultChannels("#quickirc")
	q.sendMessage("Test")