#!/usr/bin/node
const req = require('request');
const url = process.argv[2];

let count = 0;
let data;
req.get(url, (err, res) => {
  if (err) console.log(err);
  else {
    data = JSON.parse(res.body).results;
    data.forEach((obj) => {
      obj.characters.forEach((character) => {
        if (character.includes('/18/')) count++;
      });
    });
  }
  console.log(count);
});
