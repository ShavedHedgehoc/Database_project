var i=0;
var now=new Date();
ddate=now.getDate()+"/"+(now.getMonth()+1)+"/"+now.getFullYear()
document.getElementById("show_date").innerText = ddate;
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
