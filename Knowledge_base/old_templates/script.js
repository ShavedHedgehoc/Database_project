my_str="0123456789";
my_s_str=my_str.substring(1,4);
document.write("<h2>"+my_str+"</h2>");
document.write("<h2>"+my_s_str+"</h2>");  
var a=7;
document.write("<h2>"+(a==4)+"</h2>");

for(j=1; j<11; j++){
    if (j%2==0){
        document.write(j+": четное"+"</br>");
    }        
    else {
        document.write(j+": нечетное"+"</br>");
    };        
};

document.write("</br>");

var my_obj=new Object();

my_obj.x=1;
my_obj.y=2;
my_obj.z=my_obj.y+my_obj.x;

document.write("</br>");

for (pr in my_obj){
    document.write(pr+": "+ my_obj[pr]+"</br>");
};

document.write("</br>");

delete my_obj.z;

for (pr in my_obj){
    document.write(pr+": "+ my_obj[pr]+"</br>");
};

document.write("</br>");

aa=0001;
document.write(aa+"</br>");
document.write(!!aa+"</br>");
document.write("</br>");

for(j=1; j<11; j++){  
    def = j%2==0 ? ": четное" : ": нечетное"
    document.write(j+ def+"</br>");    
};
my_arr=new Array (  {x:1,y:2},
                    {x:3,y:4},
                    {x:5,y:6},
                    {x:7,y:8},
                    {x:9,y:10},
                    {x:11,y:12},
                )
for (p in my_arr){
    document.write("my_arr ["+p+"] : {");    
    for (e in my_arr[p]){        
        document.write(e+": "+my_arr[p][e]+" ");        
    }
    document.write("}</br>");    
}

i=0;
var timerId = setInterval(function(){
    i++;
    document.write("Прошло: " + i +" секунд");        
    }, 1000);
/* var count=30;
    setInterval(function() {
        count++;
        $.ajax({
            type:"GET",
            url:"test_page.html",
            data: {'count':count},
            success: function(responce){alert(responce)};
            });
        
    },1000);
 */

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
