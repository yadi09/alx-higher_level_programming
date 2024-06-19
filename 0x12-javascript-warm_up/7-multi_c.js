#!/usr/bin/node

const num = process.argv[2];

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  const ToNum = parseInt(num);
  for (let i = 0; i < ToNum; i++) {
    console.log('C is fun');
  }
}
