# -*- coding: utf-8 -*-
import random
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


@socketio.on('connect_event')
def connect_event(data):
    pass
    # socketio.emit('connect_success', 'welcome!', broadcast=False)


coordinates = {}


@socketio.on('join')
def on_join(data):
    username = data['username']
    coordinate = [random.randint(0, 1476), random.randint(0, 900)]
    socketio.emit('add_user', {'username': username, 'coordinate': coordinate}, broadcast=True)
    coordinates.update({username: coordinate})
    for key in coordinates.keys():
        socketio.emit('user_move', {'username': key, 'coordinate': coordinates.get(key)})

        # print username + ' join'
        # send(username + ' join', broadcast=True)
        # room = data['room']
        # join_room(room)
        # send(username + ' join', room=room)


@socketio.on('move')
def on_move(data):
    username = data['username']
    coordinate = data['coordinate']
    socketio.emit('user_move', {'username': username, 'coordinate': coordinate}, broadcast=True)
    coordinates.update({username: coordinate})
    # send(username + ' move to ' + json.dumps(data['coordinate']), broadcast=True)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    socketio.emit('user_leave', {'username': username}, broadcast=True)
    if coordinates.get(username):
        del coordinates[username]
    # room = data['room']
    # leave_room(room)
    # send(username + ' leave', room=room)


# 跟leave重复
# @socketio.on('disconnect')
# def on_disconnect(data):
#     username = data['username']
#     socketio.emit('user_leave', {'username': username}, broadcast=True)
#     send(username + ' leave', broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
