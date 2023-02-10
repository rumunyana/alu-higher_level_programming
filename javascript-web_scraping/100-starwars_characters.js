#!/usr/bin/node

const request = require('request');
request.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, response, body) => {
  if (err) console.log(err);
  JSON.parse(body).characters.forEach(el => {
    request.get(el, (error, res, data) => {
      if (error) console.log(err);
      console.log(JSON.parse(data).name);
    });
  });
});
