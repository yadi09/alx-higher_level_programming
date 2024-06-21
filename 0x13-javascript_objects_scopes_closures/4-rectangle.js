#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let character = '';
    let isFirstTime = false;
    for (let h = 0; h < this.height; h++) {
      if (!isFirstTime) {
        for (let w = 0; w < this.width; w++) {
          character += 'X';
        }
        isFirstTime = true;
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
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
