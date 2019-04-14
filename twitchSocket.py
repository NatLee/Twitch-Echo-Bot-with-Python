import socket


class twitchSocket(object):
    def __init__(self, channelName:str, botName:str, botAuth:str):
        self.__HOST = 'irc.twitch.tv'
        self.__PORT = 6667
        self.__NICK = botName
        self.__PASS = botAuth
        self.__CHANNEL = channelName
    
        self.__s = self.__setSocket()

        while True:
            if 'End of /NAMES list' in self.__getPacket():
                break

    def __setSocket(self) -> socket:
        s = socket.socket()
        s.connect((self.__HOST, self.__PORT))
        s.send(bytes('PASS ' + self.__PASS + '\r\n', 'UTF-8'))
        s.send(bytes('NICK ' + self.__NICK + '\r\n', 'UTF-8'))
        s.send(bytes('JOIN #' + self.__CHANNEL + '\r\n', 'UTF-8'))

        return s

    def sendMsg(self, message:str):
        self.__s.send(bytes('PRIVMSG #' + self.__CHANNEL + ' :' + message + '\r\n', 'UTF-8'))
        print(self.__NICK + ': ' + message)
    
    def __sendPong(self):
        self.__s.send(bytes('PONG :tmi.twitch.tv\r\n', 'UTF-8'))

    def __getPacket(self) -> str:
        return self.__s.recv(1024).rstrip().decode('UTF-8')
            
    def __getDataFromPacket(self) -> str:
        # rawData Sample:
        # :usr!usr@usr.tmi.twitch.tv PRIVMSG #channel :string
        rawData = self.__getPacket()
        if 'PING :tmi.twitch.tv' in rawData:
            self.__sendPong()
        # Filter the twitch send <3
        # Avoid twitch ping you without any message.
        if len(rawData.split(':')) < 3:
            return None
        return rawData

    def getMsg(self) -> tuple:
        username = None
        message = None
        try:
            rawData = self.__getDataFromPacket()
            # get message and username with extracting raw data.
            if rawData is not None:
                username = rawData.split(':')[1].split('!')[0]
                message = rawData.split(':')[2].strip()
                print(username + ': '+ message)
        except Exception as e:
            print(rawData)
            print(e)

        return username, message

