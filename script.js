let clickCount = 0;

function greetUser() {
  const nameInput = document.getElementById("nameInput");
  const outputDiv = document.getElementById("output");
  const clickCounter = document.getElementById("clickCounter");

  const name = nameInput.value.trim();
  clickCount++;

  if (name === "") {
    outputDiv.innerText = "Please enter your name before clicking!";
    outputDiv.style.color = "red";
  } else {
    outputDiv.innerText = `Hello, ${name}!`;
    outputDiv.style.color = "white";
    outputDiv.style.backgroundColor = "#222";
    outputDiv.style.borderRadius = "10px";
    outputDiv.style.padding = "20px";
  }

  clickCounter.innerText = `Button clicked: ${clickCount} times`;
}

// Add the event listener AFTER defining the function
document.getElementById("greetBtn").addEventListener("click", greetUser);
