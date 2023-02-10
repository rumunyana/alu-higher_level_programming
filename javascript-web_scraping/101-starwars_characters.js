#!/usr/bin/node

const request = require('request');
request.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, response, body) => {
  if (err) console.log(err);
  logCharacter(JSON.parse(body).characters, 0);
});

function logCharacter (characters, i) {
  if (i > characters.length - 1) {
    return;
  }
  request.get(characters[i], (error, res, data) => {
    if (error) console.log(error);
    console.log(JSON.parse(data).name);
    logCharacter(characters, i + 1);
  });
}
