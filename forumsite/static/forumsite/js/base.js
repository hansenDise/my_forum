
$(document).ready(function(){
   $("#info-login").hide();
})

$(".btn-postthread").click(function(){
   location.href="/committhreads/";
});

$("#useraccount-login").blur(function(){
    var strname = $("#useraccount-login").val();
    $.get("/check/username",
           {
            username:strname
            },
            function(data,status){
                console.log(data);
                console.log(status);
            });
});

function checkreturns(data,status){
    console.log("status:");
    console.log(status);
    console.log("data:");
    console.log(data);
}

$("#useraccount-register").blur(function(){

});

$("#email").focus(function(){
    $("#info-register").text("请填写邮箱地址");
});

$("#pwd1").focus(function(){
    $("#info-register").text("密码至少6位");
});
$("#pwd2").focus(function(){
    $("#info-register").text("密码至少6位");
});

$("#useraccount-register").focus(function(){
    $("#info-register").text("用户名以字母开头，由字母和数字组成")
});