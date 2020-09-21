#!/usr/bin/node
// Class rectangle ✅ Check if w and h are numbers greater than 0
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w !== 0 && h !== 0) && (w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
      this.print = (width, height) => {
        for (let i = 0; i < height; i++) {
          console.log('X'.repeat(width));
        }
      };
    }
  }
};
