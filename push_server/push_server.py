from time import sleep

from flask import Flask, render_template
from flask_socketio import join_room, leave_room, SocketIO, send
import json

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
    print username + ' join'
    send(username + ' join', broadcast=True)
    # room = data['room']
    # join_room(room)
    # send(username + ' join', room=room)


@socketio.on('move')
def on_move(data):
    print data
    username = data['username']
    print username + ' move to ', data['coordinate']
    send(username + ' move to ' + json.dumps(data['coordinate']), broadcast=True)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    send(username + ' leave', broadcast=True)
    # room = data['room']
    # leave_room(room)
    # send(username + ' leave', room=room)


if __name__ == '__main__':
    socketio.run(app)
