var npass = document.getElementById("password")
var npass_con = document.getElementById("password2");
var val_txt = document.getElementsByClassName("text-danger");

function valNpass(){
  if(npass.value != npass_con.value) {
    val_txt.innerHTML = '<div class="text-danger">Does not match</div>'
  } else {
    val_txt.innerHTML = '';
  }
}
npass.onchange = valNpass;
npass_con.onkeyup = valNpass;
