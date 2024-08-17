$(document).ready(function(){
    console.log("Hello World"); 
    $("#p-tag").click(function(){
        $(this).text("Paragraph has been changed").css({
            "color":"red", 
            "transition":"all 1s", 
            "background-color":"black"
        });  
    }); 
}); 