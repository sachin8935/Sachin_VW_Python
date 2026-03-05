
let clicks = 0;
let size = 16;

document.getElementById("btn").addEventListener("click", function () {
  const msg = document.getElementById("message");
  clicks++;

  if (clicks < 4) {
    size += 20;
    const colors = ["red", "blue", "green", "orange", "purple"];
    msg.style.fontSize = size + "px";
    msg.style.color = colors[Math.floor(Math.random() * colors.length)];
  } else {
    msg.innerHTML = "🎉 Happy Birthday 🎂";
    msg.classList.add("birthday-style");
    msg.style.fontSize = "";
    msg.style.color = "";

    document.getElementById("gif").innerHTML =
      '<img src="https://media.giphy.com/media/g5R9dok94mrIvplmZd/giphy.gif" width="200">';
  }
});
