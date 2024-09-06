try:
  from flask import Flask, Response, render_template
  import time
  import os
except:
  from os import *
  system("pip install flask")
  from flask import Flask, Response, render_template
  import time

app = Flask(__name__)

def generate_events():
    time.sleep(0.05)
    num = 0
    """Генерация событий в реальном времени."""
    while True:
        time.sleep(0.05)
        num += 1
        yield f"data: {num}\n\n"

@app.route('/')
def index():
    """Главная страница приложения."""
    try:
        with open("index.html", "r") as fl:
            return str(fl.read())
    except FileNotFoundError:
        return "Ошибка: файл index.html не найден.", 404

@app.route('/stream')
def stream():
    """Обработчик для события stream."""
    return Response(generate_events(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
