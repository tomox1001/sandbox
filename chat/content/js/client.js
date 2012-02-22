/**
 * Created by JetBrains WebStorm.
 * User: kawano_tomonori
 * Date: 11/12/15
 * Time: 18:41
 * To change this template use File | Settings | File Templates.
 */
$(function(){
    var socket = io.connect('http://172.22.148.31:3000');

    socket.on('connect', function() {
       console.log("connect") ;
    });

    socket.on('message', function(msg) {
        var date = new Date();
        $('#list').prepend($('<dt>' + date + '</dt><dd>' + msg + '</dd>'));
    });

    socket.on('disconnect', function() {
       console.log("disconnect") ;
    });

    $('#form').submit(function() {
        var message = $('#message').val();
        console.log("submit", message) ;
        socket.emit("chat", message);
        $('#message').attr('value', '');

        return false;
    });
});