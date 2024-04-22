#!/usr/bin/node

const size = parseInt(Number(process.argv[2]));

if (!size) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < size; i++) {
  console.log('C is fun');
}
