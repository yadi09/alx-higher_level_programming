#!/usr/bin/node

const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let character = '';
      let isFirstTime = true;
      for (let h = 0; h < this.height; h++) {
        if (isFirstTime) {
	  for (let w = 0; w < this.width; w++) {
	    character = character + c;
	  }
	  isFirstTime = false;
	}
	console.log(character);
      }
    }
  }
}
