function dismiss() {
    const targetDiv = document.getElementById("ap-user-alert");
    const btn = document.getElementsByClassName("u-close");
    if (targetDiv.style.display !== "none") {
        targetDiv.style.display = "none";
    } else {
        targetDiv.style.display = "block";
    };
}
