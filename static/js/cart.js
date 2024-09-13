$(document).ready(function(){
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
            // console.log(data); 
        }
    });
}); 