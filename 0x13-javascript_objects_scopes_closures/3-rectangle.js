#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w !== 0 && h !== 0 && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let character = '';
    let isFirstTime = true;
    for (let h = 0; h < this.height; h++) {
      if (isFirstTime) {
        for (let w = 0; w < this.width; w++) {
          character = character + 'X';
        }
        isFirstTime = false;
      }
      console.log(character);
    }
  }
};
