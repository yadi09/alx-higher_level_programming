#!/usr/bin/node

let max = 0;
let max2nd = 0;

if (!process.argv[3]) {
  console.log(max);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    const num = Number(process.argv[i]);
    if (max <= num) {
      max2nd = max;
      max = num;
    } else if (max2nd < num) {
      max2nd = num;
    }
  }
  console.log(max2nd);
}
