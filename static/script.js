const infUser = document.getElementById("infUser");

function openUserInfo() {
    infUser.style.display = 'block';
}

function closeUserInfo() {
    infUser.style.display = 'none';
}

document.getElementById("openButton").addEventListener("click", openUserInfo);
document.getElementById("closeButton").addEventListener("click", closeUserInfo);


