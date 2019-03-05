var count=30;
    setInterval(function() {
        count++;
        $.ajax({
            type:"GET",
            url:"test_page.html",
            data: {'count':count},
            success: function(responce){alert(responce)};
            });
        
    },1000);


/* setInterval(function(){
    
    $.ajax({
        type:"GET",
        url:{% 'table_renew.html' %},
        data: {},
        datatype:"",
        cache: false,
        success: function (data) {}
    });
},5000)
 */
