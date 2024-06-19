#!/usr/bin/node

const num = process.argv[2];
if (isNaN(num)) {
  console.log('Missing size');
} else {
  const ToNum = parseInt(num);
  for (let i = 0; i < ToNum; i++) {
    let str = '';
    for (let j = 0; j < ToNum; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
