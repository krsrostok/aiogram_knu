import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_request():
    # Обработка запроса от бота
    data = request.get_json()
    # Ваш код для обработки запроса и генерации ответа

    # Возвращаем ответ боту
    return 'Response'

if __name__ == '__main__':
    # Запуск сервера Flask
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

