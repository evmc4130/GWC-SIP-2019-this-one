console.log("hello world")

var i = 0;
for(i = 0; i < 21; i += 2){
   console.log(i)
}

i = 0;
while(i<=20){
  console.log(i);
  i+=2
}


function getTemp(){
  return 22.5;
}

var temperature = getTemp();
console.log(temperature)

function getTemp2(type){
  if (type == "c"){
    return 22.5;
  }
  if (type == "f"){
    return 100;
  }
}


console.log(getTemp2("c"))
console.log(getTemp2("f"))
