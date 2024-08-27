$(document).ready(function(){
    let offset = 6; 
    $("#load-more").click(function(){
        $.ajax({
            url: "{% url load_items %}", 
            data: {
                'offset':offset
            }, 
        }).done(function(response){
            response.items.forEach(function(item){
                $("#burger-testing").append("<div class='item'>" + item.item_name + '</div>'); 
            })
            console.log("Successfull in Testing for everything.")

        }).fail(function(response){
            console.log("FAILED TO GET THE DATA", response)
        }); 
    }); 
    $.ajax({
        type:"GET",
        url: "/get-data/", 
    }).done(function(response){

        response.forEach(function(item) {
            console.log(`ID: ${item.id}`);
            console.log(`Name: ${item.item_name}`);
            console.log(`Description: ${item.item_description}`);
            console.log(`Image: ${item.item_image}`);
            console.log(`Price: ${item.item_price}`);
            console.log(`Restaurant ID: ${item.restaurant_id}`);
        });

    }).fail(function(){
        console.log("error"); 
    });




});