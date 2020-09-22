#!/usr/bin/node

const fs = require('fs');

const readAFile = path => {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      console.error('An error ocurred', err);
    } else {
      console.log(data);
    }
  });
};
readAFile(process.argv[2]);
