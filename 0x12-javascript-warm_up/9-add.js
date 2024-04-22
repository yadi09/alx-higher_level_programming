#!/usr/bin/node

function add (a, b) {
  if (num1 && num2) {
    console.log(a + b);
  }
}

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

if (!num1 || !num2) {
  console.log('NaN');
} else {
  add(num1, num2);
}
