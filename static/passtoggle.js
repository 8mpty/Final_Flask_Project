function passtoggle() {
    var temp = document.getElementById("password");
        if (temp.type === "password") {
            temp.type = "text";
        }
        else {
            temp.type = "password";
        }
    }

function passtoggle_con() {
    var temp2 = document.getElementById("password2");
        if (temp2.type === "password") {
            temp2.type = "text";
        }
        else {
            temp2.type = "password";
        }
}
