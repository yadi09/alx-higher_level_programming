#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = '';
    let isFirstTime = true;
    for (let i = 0; i < this.height; i++) {
      if (isFirstTime) {
        for (let j = 0; j < this.width; j++) {
          x += 'x';
        }
        isFirstTime = false;
      }
      console.log(x);
    }
  }
}


module.exports = Rectangle;
