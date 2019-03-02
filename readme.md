Twitch Echo Bot with Python
========
[![License: GPL v3](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) [![Python 3](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/) 

Fast and easy way to use.

## Features

- Join the twitch channel.
- Send message.
- Get new message.

## Usage

```bash

git clone https://github.com/NatLee/Twitch-Echo-Bot-with-Python.git
cd ./Twitch-Echo-Bot-with-Python
python3 main.py

```

## Example (in main.py)

```python

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
```

## Contributors

[NatLee](https://github.com/NatLee/)

## License
[MIT license](./LICENSE)
