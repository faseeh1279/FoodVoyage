$(document).ready(function(){
    $(document).on("click", "#btn-add-to-cart", function(){
        cart_logo_update(); 
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
                
            }, 
            error:function(event){
                console.log(event);
            }
        })
    });
});

// Updates the Counter in the Navbar Cart 
function cart_logo_update(){
   
    $.ajax({
        url:"/cart/", 
        type:"GET", 
        success:function(data){ 
            let counter = 0; 
            data.forEach(items => {
                counter ++; 
            });
            $("#cart-number-logo").text(counter); 
        }, 
        error:function(data){
            console.log(data); 
        }
    })

}