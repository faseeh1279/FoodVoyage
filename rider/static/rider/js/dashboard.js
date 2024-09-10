$(document).ready(function () {


    $("#btn-turn-on").click(function () {
        $("#rider-dashboard").show();
        ws = new WebSocket("ws://127.0.0.1:8000/ws/sc/place_order"); 
        ws.onopen = function(event){
            console.log('Connected to the server.');
        }
        ws.onmessage = function(event){
            console.log("message received from rider"); 
        }
        ws.onclose = function(event){
            console.log("Disconnedted..."); 
        }

    });

    $("#btn-turn-off").click(function () {
        console.log("Turn off button working");
        $("#rider-dashboard").hide(); 
    });


}); 