#!/usr/bin/node

const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) console.log(err);
  fs.readFile(process.argv[3], (error, content) => {
    if (error) console.log(error);
    fs.writeFile(process.argv[4], data + content, () => {});
  });
});
