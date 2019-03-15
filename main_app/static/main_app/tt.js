var i=0;
var timerId = setInterval(function(){
    document.getElementById("message").innerText = i;
    if (i==0){
        $.ajax({
            url: "/2", // урл страницы, которую впердоливаем
            success: function(data){
                $('#table').html(data);
            }
        });        
        i=10;
    };
    i--;
}, 1000);
