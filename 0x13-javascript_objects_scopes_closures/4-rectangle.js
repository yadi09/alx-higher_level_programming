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

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
