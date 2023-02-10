#!/usr/bin/node
const argsCount = process.argv.length;
const numbers = [];
switch (argsCount) {
  case 2:
  case 3:
    console.log(0);
    break;
  default:
    for (let i = 2; i < argsCount; i++) {
      numbers.push(process.argv[i]);
    }
    numbers.sort((a, b) => b - a);
    console.log(numbers[1]);
    break;
}
