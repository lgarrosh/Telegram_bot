import socket

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к порту 80 и прослушиваем его
server_socket.bind(('0.0.0.0', 80))
server_socket.listen(5)

print("Сервер запущен и прослушивает порт 80")

while True:
    # Принимаем соединение
    client_socket, client_address = server_socket.accept()
    print(f"Соединение от {client_address}")

    # Получаем данные от клиента
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Запрос:\n{request}")

    # Формируем простой HTTP-ответ
    http_response = """HTTP/1.1 200 OK
Content-Type: text/html

<h1>Hello, World!</h1>"""

    # Отправляем ответ клиенту
    client_socket.sendall(http_response.encode('utf-8'))

    # Закрываем соединение
    client_socket.close()