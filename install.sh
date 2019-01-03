#!/bin/bash
sudo apt-get update
sudo apt install python3
sudo apt install python3-pip
sudo python3 -m pip install -r requirements.dat
sudo python3 -m run.py