#!/bin/bash
# Script to start and stop using forever.js
# To run it simply write ./run.sh in the terminal

function jumpto
{
    label=$1
    cmd=$(sed -n "/$label:/{:a;n;p;ba};" $0 | grep -v ':$')
    eval "$cmd"
    exit
}

cd /workspace/Python-telegram-bot/meme-api
forever start server.js
echo -e "\e[92m    Meme-api started working."
cd .. 
forever start -c python bot.py
echo -e "\e[92m    Dank-bot started working."

foo:
echo -e "\e[94m    Further Commands for stopping:"
echo -e "\e[39m        all = Stop both: Meme-api and Dank-bot"
echo -e "\e[39m        api = Stop Meme-api only"
echo -e "\e[39m        bot = Stop Dank-bot only"

echo -n "    Enter Commands > "
read text
if [ "$text" = 'all' ]; then
    forever stop -c python bot.py
    cd meme-api
    forever stop server.js
    cd ..
    forever list
elif [ "$text" = 'api' ]; then
    cd meme-api
    forever stop server.js
    cd ..
    forever list
    jumpto foo
elif [ "$text" = 'bot' ]; then
    forever stop -c python bot.py
    forever list
    jumpto foo
else
    echo "Unrecognized command: $text"
fi