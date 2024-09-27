# Имя виртуального окружения
VENV_DIR = venv

# Путь к файлу с зависимостями
REQUIREMENTS_FILE = requirements.txt

# Создание виртуального окружения и установка зависимостей
.PHONY: venv
venv:
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS_FILE)
# Удаление виртуального окружения
.PHONY: clean
clean:
	rm -rf $(VENV_DIR) */__pycache__ .vscode resources/rates.json


