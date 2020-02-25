# Dank Bot

Dank Bot is a simple Python bot for Telegram. It sends memes for every occasion. 

## Description
Talking to your christian parents? Need to calm the situation down with a quality meme? No problem just use the */christian* command.
Need to detect [normies](https://knowyourmeme.com/memes/normie)? Just show them a normie meme using the */normie* command and see if they laughed.
Need a random number between 1-100? no problem we've covered your back fam.
Endless possibilities, endless **Memes**.

## Dependencies and configuration

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Telegram API.

```bash
pip install pyTelegramBotAPI
```

Use the package manager [npm](https://www.npmjs.com/get-npm) to install Forever.

```bash
npm install forever -g
```
Further dependencies are specified inside *package.json* .


To configure the bot write inside *config.py* :
```python
TOKEN = 'your bot token here' 
URL = 'your meme api url here'
```
To Run the bot use.
```bash
./run.sh
```
or
```bash
node server.js
python bot.py
```
## Demo
![](https://i.imgur.com/eiAk8Ip.png)

> Standalone [API](https://node-meme-api-private.herokuapp.com/).

![](https://i.imgur.com/LBiaXel.png)

> The [Bot](https://t.me/Dankest_memed_bot).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)