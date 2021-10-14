function check(){
    var x=document.getElementById("title").value;
    var y=document.getElementById("text").value;
    if(x == ""){
        alert("需输入标题");
        return false;
    }
    if(y==""){
        alert("请输入内容")
        return false;
    }
    return true;
}