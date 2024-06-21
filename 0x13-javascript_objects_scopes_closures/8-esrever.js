#!/usr/bin/node

exports.esrever = function (list) {
  const reList = [];
  if (list) {
    for (let i = (list.length - 1); i >= 0; i--) {
      reList.push(list[i]);
    }
  }
  return (reList);
};
