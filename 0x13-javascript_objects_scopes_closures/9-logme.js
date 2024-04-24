#!/usr/bin/node

let count = 0;

exports.logMe = function counter (item) {
  console.log(`${count}: ${item}`);
    count++;
};
