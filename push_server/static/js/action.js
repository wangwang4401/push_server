/**
 * Created by Administrator on 2017/3/27.
 */

var socket = getSocket()

function joinGame() {
    var name = $("#name").val()
    if (name.length < 6 || name.length > 16) {
        alert("名字长度请保持在6-16位")
    } else {
        socket.emit('join', {username: name})
    }
}

function move() {
    var name = $("#name").val()
    var y = 0;
    var cx = parseInt(Math.random() * (1476 - y + 1) + y);
    var cy = parseInt(Math.random() * (900 - y + 1) + y);
    if (name.length < 6 || name.length > 16) {
        alert("名字长度请保持在6-16位")
    } else {
        var coordinate = [cx, cy]
        socket.emit('move', {username: name, coordinate: coordinate})
    }
}
function checkLeave() {
    var name = $("#name").val()
    if (name.length < 6 || name.length > 16) {
        alert("名字长度请保持在6-16位")
    } else {
        socket.emit('leave', {username: name})
    }
}