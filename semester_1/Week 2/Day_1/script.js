const words = [
    "javascript",
    "hangman",
    "programming",
    "developer",
    "algorithm",
];
let selectedWord = words[Math.floor(Math.random() * words.length)];
let guessedLetters = [];
let remainingGuesses = 6;

const wordDiv = document.getElementById("word");
const messageDiv = document.getElementById("message");
const lettersDiv = document.getElementById("letters");
const resetButton = document.getElementById("reset");

function resetGame() {
    selectedWord = words[Math.floor(Math.random() * words.length)];
    guessedLetters = [];
    remainingGuesses = 6;
    messageDiv.innerHTML = "";
    const buttons = document.querySelectorAll("button");
    buttons.forEach((button) => (button.disabled = false));
    displayWord();
    displayLetters();
    drawHangman();
}

function displayWord() {
    wordDiv.innerHTML = selectedWord
        .split("")
        .map((letter) => (guessedLetters.includes(letter) ? letter : "_"))
        .join(" ");
}

function displayLetters() {
    const alphabet = "abcdefghijklmnopqrstuvwxyz";
    lettersDiv.innerHTML = alphabet
        .split("")
        .map(
            (letter) =>
                guessedLetters.includes(letter)
                    ? `<button disabled>${letter}</button>`
                    : `<button onclick="guessLetter('${letter}')">${letter}</button>`
        )
        .join("");
}

function guessLetter(letter) {
    if (guessedLetters.includes(letter)) return;
    guessedLetters.push(letter);

    if (selectedWord.includes(letter)) {
        displayWord();
        checkWin();
    } else {
        remainingGuesses--;
        messageDiv.innerHTML = `Wrong guess! Remaining guesses: ${remainingGuesses}`;
        drawHangman();
        checkLose();
    }
    displayLetters(); // Update the letters display after each guess
}

function checkWin() {
    if (
        selectedWord.split("").every((letter) => guessedLetters.includes(letter))
    ) {
        messageDiv.innerHTML = "Congratulations! You won!";
        lettersDiv.innerHTML = "";
        disableAllButtons();
    }
}

function checkLose() {
    if (remainingGuesses <= 0) {
        messageDiv.innerHTML = `Game over! The word was: ${selectedWord}`;
        lettersDiv.innerHTML = "";
        disableAllButtons();
    }
}

function disableAllButtons() {
    const alphabet = "abcdefghijklmnopqrstuvwxyz";
    alphabet.split("").forEach((letter) => {
        const button = document.querySelector(`button:contains(${letter})`);
        button.disabled = true;
    });
}

displayWord();
displayLetters();

function drawHangman() {
    const canvas = document.getElementById('hangmanCanvas');
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas

    // Draw the gallows
    ctx.beginPath();
    ctx.moveTo(10, 190);
    ctx.lineTo(190, 190);
    ctx.moveTo(50, 190);
    ctx.lineTo(50, 10);
    ctx.lineTo(150, 10);
    ctx.lineTo(150, 30);
    ctx.stroke();

    if (remainingGuesses <= 5) drawHead(ctx);
    if (remainingGuesses <= 4) drawBody(ctx);
    if (remainingGuesses <= 3) drawLeftArm(ctx);
    if (remainingGuesses <= 2) drawRightArm(ctx);
    if (remainingGuesses <= 1) drawLeftLeg(ctx);
    if (remainingGuesses <= 0) drawRightLeg(ctx);
}

function drawHead(ctx) {
    ctx.beginPath();
    ctx.arc(150, 50, 20, 0, Math.PI * 2, true);
    ctx.stroke();
}

function drawBody(ctx) {
    ctx.beginPath();
    ctx.moveTo(150, 70);
    ctx.lineTo(150, 130);
    ctx.stroke();
}

function drawLeftArm(ctx) {
    ctx.beginPath();
    ctx.moveTo(150, 90);
    ctx.lineTo(120, 110);
    ctx.stroke();
}

function drawRightArm(ctx) {
    ctx.beginPath();
    ctx.moveTo(150, 90);
    ctx.lineTo(180, 110);
    ctx.stroke();
}

function drawLeftLeg(ctx) {
    ctx.beginPath();
    ctx.moveTo(150, 130);
    ctx.lineTo(130, 170);
    ctx.stroke();
}

function drawRightLeg(ctx) {
    ctx.beginPath();
    ctx.moveTo(150, 130);
    ctx.lineTo(170, 170);
    ctx.stroke();
}

window.onload = drawHangman;