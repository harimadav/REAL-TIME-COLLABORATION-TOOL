import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('text_update')
def handle_text(data):
    emit('text_update', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
    