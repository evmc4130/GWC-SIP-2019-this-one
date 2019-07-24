// console.log("hello world");

// var h1tag = document.getElementByTagName("h1")[0];
// var loc = document.getElementByClassName("headings")[3];
var adjectives = ["kind","cool","fun", "awesome"];

var pos = 0;

var loc = document.getElementById("adjective");

function changeAdj(){
  loc.innerHTML = adjectives[pos];
  pos ++
  if (pos >= adjectives.length){
    pos = 0
  }
}
var colors = [""]


var x = document.getElementsByTagName("body")[0];
function colorfulBackground(){
  x.setAttribute("style", `background-color: `

  // rgb(${Math.floor(Math.random()*256)}, ${Math.floor(Math.random()*256)}, ${Math.floor(Math.random()*256)}))
}



var fontA = "'Monoton', cursive";
var fontB = "'Sigmar One', cursive";
var fontC = "'Philosopher', sans-serif";

var allFonts = [fontA, fontB, fontC];
var pos2 = 0

var loc2 = document.getElementById("allFonts");

function changeFonts(){
  pos2 ++
  if (pos2 >= allFonts.length){
    pos2 = 0
  }
  loc2.setAttribute("style", `font-family:${allFonts[pos2]}`)
}

var colors2 = []

document.getElementById("specialfont").addEventListener("click",
  function (){
    // alert("DUUUUUUDE");
    document.getElementById("specialfont").style.color = "green"
  }
)
