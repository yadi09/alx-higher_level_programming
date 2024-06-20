#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; ++i) {
      let j = 0;
      for (; j < this.width; ++j) {
        process.stdout.write('X');
      }
      if (j === this.width) {
        console.log('');
      }
    }
  }
}

module.exports = Rectangle;
