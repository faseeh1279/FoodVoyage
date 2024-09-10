$(document).ready(function () {

    var ws = new WebSocket("ws://127.0.0.1:8000/ws/sc/place_order/");  
    ws.onopen = function(event){
        console.log('Connected to the server.',event);
        
        
    }
    ws.onmessage = function(event){
        data = JSON.parse(event.data); 
        // console.log("Order has been placed by " + jsonData.username + "Time " + jsonData.time_stamp); 
        console.log(data); 
    }
    ws.onclose = function(event){
        console.log("Disconnedted...",event); 
    }
    // $("#btn-turn-on").click(function () {
    //     $("#rider-dashboard").show();

    // });

    // $("#btn-turn-off").click(function () {
    //     console.log("Turn off button working");
    //     $("#rider-dashboard").hide(); 
    // });


}); 