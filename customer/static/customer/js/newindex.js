console.log("This is the index page of faseeh created");

    $(document).on("click", "#btn-add-to-cart", function(){
        var itemId = $(this).data('id');
        console.log(itemId)
        mydata = {
            itemId, itemId
        } 
        $.ajax({
            url: "/customer/add-to-cart/", 
            type: "POST",
            data: mydata, 
            success:function(data){
                console.log(data); 
            }, 
            error: function(xhr, status, error) {
                console.log(xhr.responseText);
            }
        }); 
    }); 



console.log("My name is anonymous"); 
