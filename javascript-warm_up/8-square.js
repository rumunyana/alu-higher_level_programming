#!/usr/bin/node

const args = process.argv.slice(2);

const num = parseInt(args[0]);

if (num) {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
} else if (num < 0) {
  console.log();
} else {
  console.log('Missing size');
}
