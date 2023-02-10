#!/usr/bin/node
exports.converter = function (base) {
  return (number = 0) => number.toString(base);
};
