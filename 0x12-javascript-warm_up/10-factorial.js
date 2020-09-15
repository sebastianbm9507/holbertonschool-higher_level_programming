#!/usr/bin/node
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
const number = Number(process.argv[2]);
console.log(factorial(number));
