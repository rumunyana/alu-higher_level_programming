#!/usr/bin/node

const args = process.argv.slice(2);

if (args[0] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(args[0]); i++) {
    console.log('C is fun');
  }
}
