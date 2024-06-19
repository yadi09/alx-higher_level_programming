#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const [, , num1, num2] = process.argv;
if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(add(parseInt(num1), parseInt(num2)));
}
