#!/usr/bin/node

let max = 0;

if (!process.argv[3]) {
  console.log(max);
} else {
  for (let i = 2; i < Number(process.argv.length); i++) {
    const num = Number(process.argv[i]);
    if (max < num) {
      max = num;
    }
  }
  console.log(max);
}
