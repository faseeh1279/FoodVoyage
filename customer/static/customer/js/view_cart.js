$(document).ready(function () {
    
   
    
    
     
    
    populate_cart();

    $(document).on("click", "#btn-delete",function(){
        const itemId = $(this).data('id');
        const row = $(this).closest("tr"); // Gets the closest tr 
        const itemPrice = Number(row.find(".item-price").text()); // Get the price of the item to remove
        let gst_total = $("#total-price"); // Get the total price element
        let currentTotal = Number(gst_total.text()); // Get the current total price

        mydata = {
            itemId: itemId
        };

        $.ajax({
            type: "POST",
            url: "/delete-data/",
            data: mydata,
            success: function (data) {
                cart_logo_update(); 
                row.remove();  // Remove the row from the table
                // Update the total price dynamically
                const newTotal = currentTotal - itemPrice;
                gst_total.text(newTotal);  // Update the total price   

            },
            error: function (data) {
                // console.log(data); 
            }
        });
    }); 


    // $("#place-order").click(function () {
        
    //     // $.ajax({
    //     //     url: "/get-cart-details/",
    //     //     type: "GET",
    //     //     success: function (data) {
    //     //         data.forEach(items => {
    //     //             // console.log(`${items.item_name}`); 
    //     //         });
    //     //     },
    //     //     error: function (data) {
    //     //         // console.log(data); 
    //     //     }
    //     // });

    // });

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
                // console.log(data); 
            }
        })
   
}




// Populates the Cart 
function populate_cart(){
    $.ajax({
        type: "GET",
        url: "/get-data/",
        success: function (data) {
            let tablebody = $("#table-body");
            let gst_total = $("#total-price");
            let price = 0;
            data.forEach(items => {
                let row =
                    `
                 <!-- Cart items will be dynamically inserted here -->
                 <tr>
                    <td>
                    <img src="/media/${items.item_image}/" style="height:80px; width:80px;">
                    </td>
                    <td>${items.item_name}</td>
                    <td class="item-price">${items.item_price}</td>
                    <td>${items.restaurant_name}</td> 
                    <td>2</td>
                    <td>${items.item_price}</td>
                    <td>
                    <button id="btn-delete" class="btn btn-danger justify-content-center" data-id="${items.id}">Remove</button>
                    </td>
                 </tr>
                `
                price = price + Number(items.item_price);
                tablebody.append(row);
            });
            gst_total.text(price);

        },
        error: function (error) {
            // console.log(error); 
        }
    });
}



