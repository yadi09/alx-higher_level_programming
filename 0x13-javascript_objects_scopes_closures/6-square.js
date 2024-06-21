#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c) {
      let character = '';
      let isFirstTime = true;
      for (let h = 0; h < this.height; h++) {
        if (isFirstTime) {
          for (let w = 0; w < this.width; w++) {
            character += c;
          }
          isFirstTime = false;
        }
        console.log(character);
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
