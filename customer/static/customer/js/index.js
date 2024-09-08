$(document).on("click", "#btn-add-to-cart", function(){
    const itemId = $(this).data('id'); 
    console.log(itemId); 
    mydata = {
        itemId: itemId, 
    }
    $.ajax({
        type: "POST",
        url: "/add-to-cart/",
        data: mydata, 
        success:function(event){
            console.log(event);
        }, 
        error:function(event){
            console.log(event);
        }
    })
}); 