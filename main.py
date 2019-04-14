from twitchSocket import twitchSocket

ts = twitchSocket(channelName='<YourChannelName>',
                  botName    ='<YourBotTwitchAccountID>', 
                  botAuth    ='<YourBotTwitchAccountAuthKey')

while True:
    try:
        username, message = ts.getMsg()
        # Your logic here.
        ts.sendMsg(message)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
