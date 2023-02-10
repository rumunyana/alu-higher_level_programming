#!/usr/bin/node
const request = require('request');

function getTasks (data, userId) {
  let count = 0;
  data.filter((element) => element.userId === userId)
    .forEach((getTasks) => {
      if (getTasks.completed === true) {
        count++;
      }
    });
  return count;
}

const url = process.argv[2];
request.get(url, (error, response) => {
  if (error) { console.log(error); }

  const data = JSON.parse(response.body);
  const users = {};
  data.forEach((element) => {
    if (users[element.userId] === undefined) {
      if (getTasks(data, element.userId) > 0) {
        users[element.userId] = getTasks(data, element.userId);
      }
    }
  });
  console.log(users);
});
