const carCompanies = ['bmw', 'audi', 'toyota'];
let carModels = ['x5 2017', 'a8', 'supra'];
let divide = (number1, number2) =>{
  return number1/number2;
}
export {carCompanies, carModels, divide};
export default divide;//syntax to declare a default method

class Circle {
  constructor(radius){
    this.radius = radius;
  }
}

export {Circle};
