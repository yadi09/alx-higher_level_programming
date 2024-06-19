#!/usr/bin/node

function secondLargeNum (args, num) {
  let nof = 0;
  let i = 0;
  while (args[i]) {
    if (args[i] > num) {
      nof++;
    }
    if (nof > 1) {
      return false;
    }
    i++;
  }
  return true;
}

const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < args.length; i++) {
    if (secondLargeNum(args, args[i])) {
      console.log(args[i]);
      break;
    }
  }
}
