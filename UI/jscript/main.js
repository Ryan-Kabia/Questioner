window.onload = function(){
    document.getElementById("comment-box").style.display="none";
    document.getElementById("comment-box2").style.display = "none";
}
function myfunc(){

    var x = document.getElementById("comment-box");
    if (x.style.display === "none") {
        x.style.display = "block";
    }
    else{
        x.style.display = "none";
    }

}

function myfunc2() {

    var x = document.getElementById("comment-box2");
    if (x.style.display === "none") {
        x.style.display = "block";
    }
    else {
        x.style.display = "none";
    }

}