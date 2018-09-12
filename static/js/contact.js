
//验证的函数
function check() {
   //1.得到要操作的表单元素(通过id获取元素)
   var name = document.getElementById("name").value;
   var mobile = document.getElementById("mobile").value;
   var zy = document.getElementById("zy").value;
   var Email = document.getElementById("Email").value;

   //获取提示信息
    var nameinfo = document.getElementById("nameinfo");
    var mobileinfo = document.getElementById("mobileinfo");
    var zyinfo = document.getElementById("zyinfo");
    var Emailinfo = document.getElementById("Emailinfo");

    /*-------------------开始验证-----------*/
    //验证姓名
    if (name==""){
        nameinfo.innerHTML="姓名不能为空"; // 将nameinfo 填充为 姓名不能为空
        return false; // 返回false 停止执行
    }else if (name.length<2 || name.length>12){
        nameinfo.innerHTML="请输入正确姓名";
        return false;
    }else {
        nameinfo.innerHTML="√";
        nameinfo.style.color="green";
    }



    //验证mobile
    if (mobile==""){
        mobileinfo.innerHTML="手机号不能为空"; // 将nameinfo 填充为 姓名不能为空
        return false; // 返回false 停止执行
    }else if ((mobile.length)!=11){    // 手机号成都 不等于 11 时
        mobileinfo.innerHTML="请输入11位手机号";
        return false;
    }else {
        mobileinfo.innerHTML="√";
        mobileinfo.style.color="green";
    }

    //验证专业zy
    if (zy==""){
        zyinfo.innerHTML="专业不能为空"; // 将nameinfo 填充为 姓名不能为空
        return false; // 返回false 停止执行
    }else if (zy.length<2 || zy.length>20){
        zyinfo.innerHTML="专业不符合规范";
        zyinfo.style.color="red";
        return false;
    }else {
        zyinfo.innerHTML="√";
        zyinfo.style.color="green";
    }

    //验证邮箱
    if (Email==""){
        Emailinfo.innerHTML="邮箱不能为空";
        return false;
    }else if(Email.indexOf("@")==-1||Email.indexOf(".")==-1){
        Emailinfo.innerHTML="邮箱格式错误";
        return false;
    }
    else {
        Emailinfo.innerHTML="√";
        Emailinfo.style.color="green";
    }
}

/*-------------------触屏事件------------*/
//验证姓名
function checkName() {
    var name = document.getElementById("name").value;
    var nameinfo = document.getElementById("nameinfo");
    if (name==""){
        nameinfo.innerHTML="姓名不能为空"; // 将nameinfo 填充为 姓名不能为空
        nameinfo.style.color="red";
        return false; // 返回false 停止执行
    }else if (name.length<2 || name.length>12){
        nameinfo.innerHTML="请输入正确姓名";
        nameinfo.style.color="red";
        return false;
    }else {
        nameinfo.innerHTML="√";
        nameinfo.style.color="green";
    }
}

//验证mobile
function checkmobile() {
    var mobile = document.getElementById("mobile").value;
    var mobileinfo = document.getElementById("mobileinfo");
    if (mobile==""){
        mobileinfo.innerHTML="手机号不能为空"; // 将nameinfo 填充为 姓名不能为空
        mobileinfo.style.color="red";
        return false; // 返回false 停止执行
    }else if ((mobile.length)!=11){    // 手机号成都 不等于 11 时
        mobileinfo.innerHTML="请输入11位手机号";
        mobileinfo.style.color="red";
        return false;
    }else {
        mobileinfo.innerHTML="√";
        mobileinfo.style.color="green";
    }
}

//验证专业 zy
function checkzy() {
    var zy = document.getElementById("zy").value;
    var zyinfo = document.getElementById("zyinfo");
    if (zy == "") {
        zyinfo.innerHTML = "专业不能为空"; // 将nameinfo 填充为 姓名不能为空
        zyinfo.style.color="red";
        return false; // 返回false 停止执行
    } else if (zy.length<2 || zy.length>20){
        zyinfo.innerHTML="专业不符合规范";
        zyinfo.style.color="red";
        return false;
    } else {
        zyinfo.innerHTML = "√";
        zyinfo.style.color = "green";
    }
}

//验证邮箱
function checkEmail() {
    var Email = document.getElementById("Email").value;
    var Emailwordinfo = document.getElementById("Emailinfo");
    if (Email == "") {
        Emailinfo.innerHTML = "邮箱不能为空";
        Emailinfo.style.color="red";
        return false;
    } else if (Email.indexOf("@") == -1 || Email.indexOf(".") == -1) {
        Emailinfo.innerHTML = "邮箱格式错误";
        Emailinfo.style.color = "red";
        return false;
    }
    else {
        Emailinfo.innerHTML = "√";
        Emailinfo.style.color = "green";
    }
}

