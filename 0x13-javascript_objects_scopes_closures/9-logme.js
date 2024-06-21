#!/usr/bin/node

exports.logMe = function (item) {
  if (!exports.logMe.count) {
    exports.logMe.count = 0;
  }

  console.log(exports.logMe.count + ': ' + item);

  exports.logMe.count++;
};
