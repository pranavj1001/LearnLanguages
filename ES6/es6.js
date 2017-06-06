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
