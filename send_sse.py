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
    return """<!DOCTYPE html>
<html>
<body>

<h1>Getting server updates</h1>
<div id="result"></div>

<script>
if(typeof(EventSource) !== "undefined") {
  var source = new EventSource("stream");
  source.onmessage = function(event) {
    document.getElementById("result").innerHTML = event.data;
  };
} else {
  document.getElementById("result").innerHTML = "Sorry, your browser does not support server-sent events...";
}
</script>

</body>
</html>"""

@app.route('/stream')
def stream():
    """Обработчик для события stream."""
    return Response(generate_events(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
