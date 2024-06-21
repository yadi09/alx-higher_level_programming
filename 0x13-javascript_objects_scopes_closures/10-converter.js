#!/usr/bin/node

exports.converter = function (base) {
  return function (num) {
    if (base >= 2 || base <= 36) {
      return num.toString(base);
    }
  };
};
