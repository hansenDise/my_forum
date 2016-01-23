$(document).ready(function(){
   $("#info-login").hide();
})

$(".btn-postthread").click(function(){
   location.href="/committhreads/";
});

$("#useraccount-login").change(function(){
    var strname = $("#useraccount-login").val();
    $.get("/check/username",
           {
            username:strname
            },
            function(data,status){
                if (status == 'success') {
                    
                }
                else {
                    $("#info-login").text("连接服务器失败.请稍后再试!");
                    $("#info-login").show();
                }
            });
});

function checkreturns(data,status){
    console.log("status:");
    console.log(status);
    console.log("data:");
    console.log(data);
}

$("#useraccount-register").change(function(){
    var name = $("#useraccount-register").val();
    var reg = new RegExp("[a-zA-Z][a-zA-Z0-9]{5,}");
    if (!reg.test(name)) {
        $("#useraccount-register").addClass("register-login-warning");    
    }
    else {
        $("#useraccount-register").removeClass("register-login-warning");
    }
    $("#info-register").text("用户名以字母开头，由至少6个字母和数字组成");
});

$("#email").change(function(){
    $("#info-register").text("请填写邮箱地址");
});

$("#pwd1").change(function(){
    $("#info-register").text("密码至少6位");
});
$("#pwd2").change(function(){
    $("#info-register").text("密码至少6位");
});

// button click to submit register data
$("#btn-register").click(function(){
    var namereg = new RegExp("[a-zA-Z][a-zA-Z0-9]{5,}");
    var name = $("#useraccount-register").val();
    if(name.length <6) {
        console.log("name.length= ",name.length);
        $("#useraccount-register").change();
        return -1;
    }
    if(!namereg.test(name)) {
        console.log("test return false");
        $("#useraccount-register").change();
        return -1;
    }
    
    var passwd1 = $("#pwd1").val();
    var passwd2 = $("#pwd2").val();
    if (passwd1.length < 6 || passwd2.length < 6 || passwd1 != passwd2) {
        console.log("password1:",passwd1," password2 = ",passwd2);
        $("#pwd1").change();
        $("#pwd2").change();
        return -1;
    }
    $("#form-register").submit();
});