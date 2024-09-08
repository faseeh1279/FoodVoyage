$(document).ready(function(){
    $.ajax({
        url:"/cart/", 
        type:"GET", 
        success:function(data){

        }, 
        error:function(data){
            
        }
    })
}); 