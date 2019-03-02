Twitch Echo Bot with Python

Features
========

- Join the twitch channel.
- Send message.
- Get new message.

How to use (in main.py)
==========

.. code:: python

  from twitchSocket import twitchSocket

  ts = twitchSocket(channelName='<YourCannelName>',
                    botName    ='<YourBotAccountName>', 
                    botAuth    ='<YourBotAccountTwitchAuthKey')

  while True:
        try:
            username, message = ts.getMsg()
            # Your logic here.
            ts.sendMsg(message)

        except(KeyboardInterrupt, EOFError, SystemExit):
            break

