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

//create an instance of Rectangle1
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
//create an instance of Circle
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

//Prototypes
//Every JavaScript object has a prototype. The prototype is also an object.
//All JavaScript objects inherit their properties and methods from their prototype.
function shipInfo(name, type, inServiceSince){
  this.name = name;
  this.type = type;
  this.inServiceSince = inServiceSince;

  this.numberOfFloors = (floors) => `${this.name} has ${floors} floors.`;

}
//add another property
shipInfo.prototype.numberofCrewMembers;
//add another property function
//Can't use arrow function here because arrow functions don't create 'this' object for the function prototype to reference
//therefore use the normal function
shipInfo.prototype.info = function(companyName){
  return `${this.name} is owned by ${companyName}`;
};
//create an instance
let ship1 = new shipInfo("Oasis of the Seas", "Cruise Ship", "2009");
ship1.numberofCrewMembers = 750;
//console.log(ship1);
//console.log(ship1.numberOfFloors(20));
//console.log(ship1.info("Royal Caribbean International"));

//Data Structures
// 1) Set -> similar to array but can only store unique values.
let set = new Set();
//add method
//integers
set.add(30);
set.add(13);
set.add(12);
//strings
set.add("string");
//objects
set.add({firstObject: 60, secondObject: 70});
//console.log(set);
//console.log(set.size);// to know the size
//console.log(set.has("string"));// to check for an element
//to convert an array to set
let flowers = ["rose", "lily", "daffodils"];
let flowersSet = new Set(flowers);
//console.log(flowers);
//console.log(flowersSet);
//to traverse through the set
for (let element of flowersSet.values()){
  //console.log(element);
}
//trick to get unique elements from a string
let sentence = "fansakjvbjvbsdhvhbsdhvbabvjabjaisoalkmz,nawnfkjgvnajkfalmaskldmasdm";
let sentenceArray = sentence.split("");
let sentenceSet = new Set(sentenceArray);
//console.log(sentenceArray);
//console.log(sentenceSet);

// 2) Maps -> has keys and values. Each key is unique.
let map = new Map();
//map.set method takes two Parameters: key and value
//strings as keys
let keyOfMap = "SampleKey";
let valueOfMap = "SampleValue";
map.set(keyOfMap, valueOfMap);
map.set("SampleKey1", "SampleValue1");
//object as a key
let keyOfMap2 = {sampleObject: 'SampleKey2'};
map.set(keyOfMap2, "SampleValue2");
//function as a key
let keyOfMap3 = function() {};
map.set(keyOfMap3, "SampleValue3");
//console.log(map);
//convert an array to a Map
let numberArray1 = [[1, 'one'], [2, 'two'], [3, 'three']];
let numberSet = new Map(numberArray1);
//console.log(numberSet);
//to traverse through the map
for (let [key, value] of numberSet.entries()){
  //console.log(`${key} => ${value}`);
}
//trick to get unique elements from a string
let sentence1 = "jahbahbchabcjksaufgabshjabchabnzbchuyasbfabncjhbahbshcbsajkcbashbcvjhasb";
let sentence1Map = new Map();
let currentLetter;
for( let i = 0; i < sentence1.length; i++){
  currentLetter = sentence1[i];
  if(!(sentence1Map.has(currentLetter))){ // similar to if(sentence1Map.has(currentLetter) == false) // if the currentLetter is not in the map
    sentence1Map.set(currentLetter, 1);
  }else{ // if the currentLetter has already been added to the map then update its count value
    sentence1Map.set(currentLetter, sentence1Map.get(currentLetter) + 1);
  }
}
//console.log(sentence1Map);

//Closures
//A closure is the combination of a function and the lexical environment within which that function was declared.
//we can create function factories and private data with Closures
let sampleFunction = () => {
  let data = "Dovahkiin"; //data is a local variable created by sampleFunction
  let logData = () => { //logData() is the inner function, a closure
    //console.log(data); //use variable declared in the parent function
  }
  logData();
}
//console.log(data); //will throw an error
sampleFunction();

//Function Factories
//In this example, we have defined a function makeAdder(x), which takes a single argument, x, and returns a new function.
//The function it returns takes a single argument, y, and returns the sum of x and y.
//In essence, makeAdder is a function factory — it creates functions which can add a specific value to their argument.
// let makeAdder = (x) => {
//   // can make it shorter, thanks to ES6
//   // return (y) => {
//   //   return x + y;
//   // };
//   return y => x + y;
// }
// can make it further shorter, thanks to ES6
let makeAdder = (x) => (y) => x + y;
let add5 = makeAdder(5);
let add10 = makeAdder(10);
//console.log(add5(2));  // 7
//console.log(add10(2)); // 12

//Private Methods -> used to restrict access
const account = () => {
  let amount = 0;
  let editAmount = (value) => {
    return amount += value;
  }
  const editAccount = (changeAmount) => editAmount(changeAmount);
  const checkAccount = () => amount;
  // return {
  //   editAccount: editAccount,
  //   checkAccount: checkAccount
  // }
  //or
  return { editAccount, checkAccount }
}
let currentAmount = account();
//console.log(currentAmount);
currentAmount.editAccount(50);
//console.log(currentAmount.checkAccount());
currentAmount.editAccount(-10);
//console.log(currentAmount.checkAccount());

//Generators
//The function* declaration (function keyword followed by an asterisk) defines a generator function, which returns a Generator object.
function* idMaker() {
  let index = 0;
  while (index < 3)
    yield index++;
}
let gen = idMaker();
// console.log(gen.next().value); // 0
// console.log(gen.next().value); // 1
// console.log(gen.next().value); // 2
// console.log(gen.next().value); // undefined
