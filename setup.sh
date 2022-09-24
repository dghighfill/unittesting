#!/bin/bash

python -m venv .venv

.venv/Scripts/python.exe -m pip install --upgrade pip
.venv/Scripts/pip3 install pip --upgrade
.venv/Scripts/pip install -r requirements.txt