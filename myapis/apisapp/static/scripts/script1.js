const sendCoins = document.getElementById("sendCoins");
const buyCoins = document.getElementById("buyCoins");
const coinUsers = document.getElementById("coinUsers");
const coinLogins = document.getElementById("coinLogins");
buyCoins.style.display = "none";
coinUsers.style.display = "none";
coinLogins.style.display = "none";
sendCoins.style.display = "block";

function buyCoin(){
    sendCoins.style.display = "none";
    coinUsers.style.display = "none";
    coinLogins.style.display = "none";
    buyCoins.style.display = "block";
}
function sendCoin(){
    buyCoins.style.display = "none";
    coinUsers.style.display = "none";
    coinLogins.style.display = "none";
    sendCoins.style.display = "block";

}
function coinUser(){
    sendCoins.style.display = "none";
    buyCoins.style.display = "none";
    coinLogins.style.display = "none";
    coinUsers.style.display = "block";
}
function coinLogin(){
    sendCoins.style.display = "none";
    buyCoins.style.display = "none";
    coinLogins.style.display = "block";
    coinUsers.style.display = "none";

}