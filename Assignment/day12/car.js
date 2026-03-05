

let position = 0;

document.getElementById("moveBtn").addEventListener("click", () => {
  position += 50;
  document.getElementById("car").style.left = position + "px";
});
