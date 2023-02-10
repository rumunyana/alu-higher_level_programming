#!/usr/bin/node

const fact = parseInt(process.argv.slice(2)[0]);

if (isNaN(fact) === true) {
  console.log(1);
} else {
  const result = Factorial(fact);
  console.log(result);
}

function Factorial (num) {
  if (num === 1) {
    return 1;
  } else {
    return (num * Factorial(num - 1));
  }
}