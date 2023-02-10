#!/usr/bin/node

const args = process.argv.slice(2);

const number = parseInt(args[0]);

if (number === undefined) {
  console.log('Not a number');
} else {
  if (isNaN(number)) {
    console.log('Not a number');
  } else {
    if (typeof (number) === 'number') {
      console.log('My number: ' + number);
    }
  }
}
