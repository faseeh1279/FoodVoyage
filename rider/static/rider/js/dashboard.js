$(document).ready(function () {
    
    // $("#btn-turn-on").click(function () {
    //     $("#rider-dashboard").show();

    // });

    // $("#btn-turn-off").click(function () {
    //     $("#rider-dashboard").hide(); 
    // });


}); 

var ws = new WebSocket("ws://127.0.0.1:8000/ws/sc/place_order/");  
    ws.onopen = function(event){
        console.log('Connected to the server.',event);
        
        
    }
    ws.onmessage = function(event){
        let data = JSON.parse(event.data); 
        console.log("Order has been placed by " + data.username + "Time " + data.time_stamp); 
        
    }
    ws.onclose = function(event){
        console.log("Disconnedted...",event); 
    }