#!/usr/bin/node

const args = process.argv;
if (isNaN(args[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[2]));
}
