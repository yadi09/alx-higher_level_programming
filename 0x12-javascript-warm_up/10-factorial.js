#!/usr/bin/node

function factorial (num) {
  if (num > 0) {
    return (factorial(num - 1) * num);
  }
  return (1);
}

const num = process.argv[2];
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(parseInt(num)));
}
