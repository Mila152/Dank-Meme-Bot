#!/bin/bash
forever stop -c python bot.py
cd meme-api
forever stop server.js
forever list