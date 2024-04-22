#!/usr/bin/node

const num = Number(process.argv[2]);
if (num) {
  console.log('My number:', parseInt(num));
} else {
  console.log('Not a number');
}
