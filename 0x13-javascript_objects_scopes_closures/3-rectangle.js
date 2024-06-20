#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      let x = '';
      let isFirstTime = false;
      for (let i = 0; i < this.height; i++) {
        if (isFirstTime) {
          for (let j = 0; j < this.width; j++) {
            x += 'x';
          }
          isFirstTime = true;
        }
        console.log(x);
      }
    }
  }
}

module.exports = Rectangle;
