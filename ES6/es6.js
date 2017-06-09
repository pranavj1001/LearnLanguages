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

//Spread Operators
//one simply pass an array with Spread Operators
let array1 = [10, 20, 30, 40];
let array2 = [...array1, 50, 60];//value of array1 is spreaded in array2
//console.log(array2);

//Rest Parameters
//similar to Spread Operators
function getNumbers(...array3){
  //console.log(array3);
}
//getNumbers(array2);
getNumbers(2, 5, 7 , 8, 9);

//Destructuring Assignments
//The destructuring assignment syntax is a JavaScript expression that makes it possible to unpack values from arrays, or properties from objects, into distinct variables.
//for arrays
let array4 = [1, 2, 3];
//the traditional way
//let one = array4[0];
//let two = array4[1];
//with Destructuring Assignments
let [one, twos] = array4;
//console.log(one, twos);
//for objects
let person = {name: 'Dovah', heightInCm: '180', weightInKg: '82'};
//the traditional way
//let heightInCm = person.heightInCm;
//let weightInKg = person.weightInKg;
//Destructuring Assignments
//let {heightInCm, weightInKgs} = person; wont work, the names should match the names in the objArray
let {heightInCm, weightInKg} = person;
//console.log(heightInCm, weightInKg);

//Arrow function
//Arrow Functions are considered to be Anonymous by default
//the traditional Anonymous function expression
// var greet = function() {
//   console.log("Hello");
// }
//the Anonymous arrow function expression
//similarly you can also define arrow functions for other Anonymous functions like the one in setTimeout(()=>{},timeInMSecs);
//just remember the '=>'
var greet  = () => {
  //console.log("Hola");
}
greet();
