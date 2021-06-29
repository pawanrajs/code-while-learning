var colors = generateRandomColors(6);
var squares = document.querySelectorAll(".square");
var picked = pickColor();
var messageDisplay = document.querySelector("#message");
var resetButton = document.querySelector("#reset");
var heading1 = document.querySelector("h1");
var hardbutton = document.querySelector("#hardbutton");
var easybutton = document.querySelector("#easybutton");
var numsquares = 6;

var pickedColorDisplay = document.getElementById("pickedCD");
pickedColorDisplay.textContent = picked;

for (var i = 0; i < squares.length; i++) {
    //initial colors
    squares[i].style.backgroundColor = colors[i];

    //event listeners
    squares[i].addEventListener("click", function() {
        var clicked = this.style.backgroundColor;
        if (clicked === picked) {
            messageDisplay.textContent = "Correct!";
            resetButton.textContent = "Play Again";
            for (var i = 0; i < squares.length; i++) {
                squares[i].style.backgroundColor = picked;
            }
            heading1.style.backgroundColor = picked;
        } else {

            //use getComputedStyle to get CSS background color value and set it
            //instead of hardcoding it.
            messageDisplay.textContent = "Try Again!";
            var bodyElementStyle = getComputedStyle(document.querySelector("body"));
            this.style.backgroundColor = bodyElementStyle.getPropertyValue("background-color");
        }
    });
}

function pickColor() {
    var pickIndex = Math.floor(Math.random() * colors.length);
    return colors[pickIndex];
}

function generateRandomColors(num) {
    colorArray = [];
    for (i = 0; i < num; i++) {
        colorArray.push(getRandomColor());
    }
    console.log(colorArray);
    return colorArray;
}

function getRandomColor() {
    randomColor = "rgb(";
    for (var i = 0; i < 3; i++) {
        randomColor += Math.floor(Math.random() * 256);
        i === 2 ? randomColor += ")" : randomColor += ", ";
    }
    console.log(randomColor);
    return randomColor;
}

resetButton.addEventListener("click", function() {
    //generate new colors
    colors = generateRandomColors(numsquares);
    //pick new random color
    picked = pickColor();
    //change colors of squares
    for (var i = 0; i < colors.length; i++) {
        squares[i].style.backgroundColor = colors[i];
    }

    //display change
    pickedColorDisplay.textContent = picked;
    this.textContent = "New Colors";
    heading1.style.backgroundColor = "";
    messageDisplay.textContent = "";
});

easybutton.addEventListener("click", function() {
    easybutton.classList.add("selected");
    hardbutton.classList.remove("selected");
    numsquares = 3;
    heading1.style.backgroundColor = "";
    messageDisplay.textContent = "";

    colors = generateRandomColors(numsquares);
    picked = pickColor();
    pickedColorDisplay.textContent = picked;
    for (var i = 0; i < squares.length; i++) {
        if (colors[i]) {
            squares[i].style.backgroundColor = colors[i];
            squares[i].style.display = "block";
        } else {
            squares[i].style.display = "none";
        }
    }
});

hardbutton.addEventListener("click", function() {
    easybutton.classList.remove("selected");
    hardbutton.classList.add("selected");
    numsquares = 6;
    heading1.style.backgroundColor = "";
    messageDisplay.textContent = "";

    colors = generateRandomColors(numsquares);
    picked = pickColor();
    pickedColorDisplay.textContent = picked;
    for (var i = 0; i < squares.length; i++) {
        if (colors[i]) {
            squares[i].style.backgroundColor = colors[i];
            squares[i].style.display = "block";
        } else {
            squares[i].style.display = "none";
        }
    }
});