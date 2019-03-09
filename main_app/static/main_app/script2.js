var i=0;
var timerId = setInterval(function(){
    // i++;
    // document.getElementById("table").innerHTML = i;
    $.ajax({
        url: "/2", // урл страницы, которую впердоливаем
        success: function(data){
            $('#table').html(data);
        }
    })}, 10000);
