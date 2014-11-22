quickIRC
========

[![Code Health](https://landscape.io/github/shortdudey123/quickIRC/master/landscape.svg)](https://landscape.io/github/shortdudey123/quickIRC/master)

Introduction
------------

quickIRC serves to allow messages to be quickly and easily posted to given channels on an IRC server.

Example Uses
------------

* Monitoring scripts
* Automated script error output
* Posting cron job results
* Report the start and end of a job or script

Notes
-----

If the IRC network you are connecting to is globally distributed, the connectDelay may need to be as high as 5 seconds.  (Example - Freenode needs 4-5 seconds)  For local or geographically located servers the delay can be less.  Individual results will very so testing of different values should be done before this is fully implemented.

References
----------
* [IRC Python Bot: Best Way](http://stackoverflow.com/questions/1100840/irc-python-bot-best-way)
* [How do i program a simple IRC bot in python?](http://stackoverflow.com/questions/2968408/how-do-i-program-a-simple-irc-bot-in-python)
* [Developing a Basic IRC Bot with Python](http://forum.codecall.net/topic/59608-developing-a-basic-irc-bot-with-python/)
