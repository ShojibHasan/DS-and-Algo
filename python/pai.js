// var num = 22/7;
// var n = num.toFixed(100);
// console.log(n)

const num = BigInt(22);
const den = BigInt(7);
const scale = BigInt(10) ** BigInt(1000); 

let result = num * scale / den; 

let resultStr = result.toString();
resultStr = resultStr.slice(0, resultStr.length - 1000) + '.' + resultStr.slice(resultStr.length - 1000);

console.log(resultStr);