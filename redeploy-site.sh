#!/bin/bash

tmux kill-server
cd personal-portfolio
git fetch && git reset origin/main --hard
virtualenv env
source env/bin/activate
pip install -r requirements.txt
tmux new -d 'source env/bin/activate && flask run --host=0.0.0.0'
cd
clear 
