#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const id = process.argv[3];
const fs = require('fs');
request.get(url, async (error, body) => {
  error
    ? console.log(error)
    : await fs.writeFile(id, body.body, (err) => {
      if (err) { console.log(err); }
    });
});
