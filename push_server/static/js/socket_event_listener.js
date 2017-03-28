/**
 * Created by Wpj on 2017/3/27.
 */
var socket = io.connect('http://localhost:5000');
socket.on('connect', function () {
    socket.emit('connect_event', {data: 'user connect'});
});


// 添加一个连接监听器
socket.on('connect_success', function (data) {
    $("#result").append(data + "<br />")
    // data = JSON.stringify(data) object转string
});


// socket.on('emitMessage', function (data) {
//     document.getElementById("result").innerHTML += data + "<br />";
// });


socket.on('add_user', function (data) {
    $("#result").append(data["username"] + " add <br />")
    var coordinate = data["coordinate"]
    // 动态增加控件
    $("#GameBoard").append("<div id=\"" + data["username"] + "\">" + data["username"] + "</div>")
    $("#" + data["username"]).css("position", "relative")
    $("#" + data["username"]).css("background-color", "red")
    $("#" + data["username"]).css("width", "80px")
    $("#" + data["username"]).css("height", "80px")
    $("#" + data["username"]).css("left", coordinate[0] + "px")
    $("#" + data["username"]).css("top", coordinate[1] + "px")
});

socket.on('user_move', function (data) {
    if ($("#" + data["username"]).length < 1)
    {
        $("#GameBoard").append("<div id=\"" + data["username"] + "\">" + data["username"] + "</div>")
        $("#" + data["username"]).css("position", "relative")
        $("#" + data["username"]).css("background-color", "red")
        $("#" + data["username"]).css("width", "80px")
        $("#" + data["username"]).css("height", "80px")
    }
    $("#result").append(data["username"] + " move to " + data["coordinate"] + "<br />")
    $("#" + data["username"]).css("left", data["coordinate"][0] + "px")
    $("#" + data["username"]).css("top", data["coordinate"][1] + "px")
    // 根据username 移动控件的相对位置
});

socket.on('user_leave', function (data) {
    if ($("#" + data["username"]).length > 0)
    {
        $("#result").append(data["username"] + " leave <br />")
        $("#" + data["username"]).remove()
    }
    // 移除相应控件
});


// 添加一个关闭连接的监听器
// socket.on('disconnect', function () {
//     socket.emit('leave', {username: $("#name").val()})
// });


// 通过Socket发送一条消息到服务器
function sendMessageToServer(message) {
    socket.send(message);
}

function getSocket() {
    return socket
}




