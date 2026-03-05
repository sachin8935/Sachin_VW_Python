

let stressPos = 0;
let peacePos = 0;
let collided = false;

function checkCollision() {
  if (stressPos >= 260 && peacePos >= 260 && !collided) {
    collided = true;

    // fall animation
    document.getElementById("stress").classList.add("fall");
    document.getElementById("peace").classList.add("fall");

    // show message after delay
    setTimeout(() => {
      const msg = document.getElementById("message");
      msg.style.display = "block";
      msg.style.opacity = "1";
    }, 1500);
  }
}

function moveStress() {
  if (collided) return;

  stressPos += 20;
  document.getElementById("stress").style.left = stressPos + "px";
  checkCollision();
}

function movePeace() {
  if (collided) return;

  peacePos += 20;
  document.getElementById("peace").style.right = peacePos + "px";
  checkCollision();
}

