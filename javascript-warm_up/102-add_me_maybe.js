#!/usr/bin/node
const addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
module.exports = {
  addMeMaybe
};
