#!/usr/bin/node

const args = process.argv;
const nul = 'undefined';
if (args.length >= 3) {
  console.log(args[2] + ' is ' + args[3]);
} else if (args.length >= 2) {
  console.log(args[2] + ' is ' + nul);
} else {
  console.log(nul + ' is ' + nul);
}
