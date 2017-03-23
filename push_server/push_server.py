from time import sleep

from flask import Flask, render_template
from flask_socketio import join_room, leave_room, SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@socketio.on('my event')
def my_event(message):
    print(message['data'])
    send('66666', broadcast=True)


# @socketio.on('connect')
# def my_event(message):
#     print(message['data'])

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' join', room=room)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' leave', room=room)


if __name__ == '__main__':
    socketio.run(app)
