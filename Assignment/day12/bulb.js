
const bulb = document.getElementById("bulb");

document.getElementById("onBtn").addEventListener("click", () => {
  bulb.src = "https://www.w3schools.com/js/pic_bulbon.gif";
});

document.getElementById("offBtn").addEventListener("click", () => {
  bulb.src = "https://www.w3schools.com/js/pic_bulboff.gif";
});
