#!/usr/bin/node

const nums = process.argv.slice(2);
let max = 0;
let max2nd = 0;
let num = 0;

for (let i = 0; i < nums.length; i++) {
  num = Number(nums[i]);
  if (num > max) {
    max2nd = max;
    max = num;
  }
}
console.log(max2nd);
