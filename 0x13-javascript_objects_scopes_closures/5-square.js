#!/usr/bin/node

const rect = require('./4-rectangle');

module.exports = class Square extends rect {
  constructor (size) {
    super(size, size);
  }
};
