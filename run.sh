#!/bin/bash

export PYTHONPATH=$(pwd)

pip install -r requirements.txt

# Запускаем приложение
python3 source/main.py