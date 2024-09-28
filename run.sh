#!/bin/bash

# Создаем виртуальное окружение
make venv

# Активируем виртуальное окружение
source venv/bin/activate

export PYTHONPATH=$(pwd)

# Запускаем приложение
exec python source/main.py