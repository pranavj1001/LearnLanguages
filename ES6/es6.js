console.log("Pranav Jain here");

//simple ES5 var declaration
var limit = 1000;
//console.log(limit);

//ES6 var declaration
let newLimit = 10000;
newLimit += 100;//you can change the value of the 'let' var
//console.log(newLimit);

//ES6 const var declaration
const absoluteLimit = 100000;
//absoluteLimit += 1100; will show error
//console.log(absoluteLimit);

//not able to change data doesn't prevent us from manipulating the data
const fruits = ['apple', 'mango', 'strawberry'];
fruits.push('pineapple');//you cannot reassign data but you can add data
//console.log(fruits);

//Block Scoping
//advantage of 'let'
let var1 = 10;

{
  let var1 = 100;
  //console.log('Block var1', var1);
}

//console.log('original var1', var1);
//Output:
//Block var1 10
//original var 10
//let supports Block Scoping

//if we were using the old style ie 'var'
var var2 = 20;

{
  var var2 = 50;
  //console.log('Block var2', var2);
}

//console.log('original var2', var2);
//Output:
//Block var2 50
//original var2 50
//var doesn't support Block Scoping

//if we use the const type declaration
const var3 = 30;

{
  const var3 = 300;
  //console.log('Block var3', var3);
}
//console.log('original var3', var3);
//Output:
//Block var3 30
//original var3 300
//const supports Block Scoping

//Template Literals
//referred to strings that have embedded expressions within them
let companyName = 'bmw';
let carName = companyName + ' x5';//traditional method
//console.log(carName);
let fullCarName = `${companyName} x5`;//Template Literal is used here. Note you have to use `` and not this ''
//console.log(fullCarName);
