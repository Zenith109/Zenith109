// weather charts //
var kelvin = 293;
// Celsius is always 273 colder //
const celsius = kelvin - 273;
// Farhrenheit to Celsius //
let fahrenheit = celsius * (9/5) + 32;
// Rounds up //
fahrenheit = Math.floor(fahrenheit);

console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);