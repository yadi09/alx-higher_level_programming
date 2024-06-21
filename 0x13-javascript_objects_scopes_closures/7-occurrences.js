#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  if (list && searchElement) {
    list.forEach(function (num) {
      if (num === searchElement) {
        count++;
      }
    });
  }

  return (count);
};
