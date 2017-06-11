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
let greet  = () => {
  //console.log("Hola");
}
greet();

//Helper Methods
//Types of Helper Methods
// 1) Map Helper Metods
let numberArray = [10, 20, 30];
// let square = (number) => {
//   return number * number;
// }
// let squaredArray = numberArray.map(square);
// or
let squaredArray = numberArray.map((number) => number * number );
//console.log(squaredArray);
// 2) Filter Helper Methods
let fruitPrices = [12, 15, 25, 10, 19, 22];
let reasonableFruitPrices = fruitPrices.filter((price) => price <= 15);
//console.log(reasonableFruitPrices);

//String Helper Methods
// 1) Repeat Method
//used to create a large string by just concatenating string a number of times
//let stringToRepeat = "Witcher 3  is the" + "e".repeat(3) + " game" + "!".repeat(5);
//let us use the Template Literals
let stringToRepeat = `Witcher 3  is the${"e".repeat(3)} game${"!".repeat(5)}`;
//console.log(stringToRepeat);
// 2) startsWith and endsWith
//will return a boolean value
//console.log(stringToRepeat.startsWith("Witcher"));//O/P -> true//endsWith is similar except the obvious change.
// 3) includes
//will return a boolean value
//just search for the string in a string
//console.log(stringToRepeat.includes("ee"));//O/P -> true

//check numbers
// 1) isFinite helps to validate our code to help us to not to break our code
let luggageInfo = (name, weight) => {
  return Number.isFinite(weight);
}
// console.log(luggageInfo('mobile', Infinity));//O/P -> false
// console.log(luggageInfo('mobile', 45));//O/P -> true
// console.log(luggageInfo('mobile', Math.pow(9, 67)));//O/P -> true

// 2) isSafeInteger, in above isFinite returned true when put the weight as 9^67 but JS handles numbers only upto 2^53, so 9^67 cannot be handled in usual manners and thus its not a safe isSafeInteger
let safeLuggageInfo = (name, weight) => {
  return Number.isSafeInteger(weight);
}
// console.log(safeLuggageInfo('mobile', Math.pow(9, 67)));//O/P -> false

//Modules
//Modules refer to reusable pieces of code in our application.
//they appear independently in their own separate files
import {carCompanies, carModels, divide} from './exampleModule'
//import divie from './exampleModule' //syntax to get the default method
//console.log(carCompanies, carModels);
//console.log(divide(4,2));

//Class
//Classes are "special functions", and just as you can define function expressions and function declarations, the class syntax has two components: class expressions and class declarations
//Unlike Functions, classes are not hoisted
//this will throw an error
// var p = new Rectangle(); // ReferenceError
// class Rectangle {}
//Class Declaration:
class Rectangle1 {
  constructor(height, width, colour) {
    this.height = height;
    this.width = width;
    this.colour = colour;
  }
  getColour() {
    console.log(`The rectangle with ${this.height}cm height and ${this.width}cm width has a ${this.colour} colour`);
  }

};
//Similar to function expressions, here also we have Class Expressions:
// unnamed
var Rectangle2 = class {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
};
// named
var Rectangle = class Rectangle3 {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
};
let rectABCD = new Rectangle1(23, 18, "red");
//console.log(rectABCD);
//rectABCD.getColour();

//Inheritance in classes
class RoundedRectangle extends Rectangle1 {
  constructor(height, width, colour, cornerRadius){
    super(height, width, colour);
    this.cornerRadius = cornerRadius;
  }
  getColour(){
    console.log(`The roundRectangle with ${this.height}cm height ${this.width}cm width and ${this.cornerRadius}cm cornerRadius has a ${this.colour} colour`);
  }
}

let roundRectEFGH = new RoundedRectangle(27, 89, "blue", 6);
//console.log(roundRectEFGH);
//roundRectEFGH.getColour();
import {Circle} from './exampleModule';//imported class from exampleModule.js
let circleO = new Circle(56);
//console.log(circleO);

//Static Methods in Classes
//The static keyword defines a static method for a class. Static methods are called without instantiating their class and cannot be called through a class instance. Static methods are often used to create utility functions for an application.
class Square {
  static area(sideLength){
    return sideLength*sideLength;
  }
}
let squareABCD = Square.area(56);
//console.log(squareABCD);
