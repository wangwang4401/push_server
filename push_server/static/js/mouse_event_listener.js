/**
 * Created by Wpj on 2017/3/28.
 */
var socket = getSocket()
$("#GameBoard").ready(function () {
    $("#GameBoard").mousemove(function (e) {
        var name = $("#name").val()
        var left = $("#GameBoard").offset().left
        var top = $("#GameBoard").offset().top
        $("#" + name).css("left", e.pageX - left)
        $("#" + name).css("top", e.pageY - top)
        socket.emit('move', {username: name, coordinate: [e.pageX - left, e.pageY - top]})
    })
})
