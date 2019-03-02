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
