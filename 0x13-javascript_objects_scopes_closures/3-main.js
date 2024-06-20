#!/usr/bin/node
const Rectangle = require('./3-rectangle');

const r1 = new Rectangle(3, 3);
r1.print();

console.log('---');

const r2 = new Rectangle(3, 10);
r2.print();

console.log('---');

const r3 = new Rectangle(10, 3);
r3.print();
