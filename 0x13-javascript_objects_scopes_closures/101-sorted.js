#!/usr/bin/node
// computes a dictionary of user ids by occurrence.
const { dictImpo } = require('./101-data');
const newdict = {};
for (const key in dictImpo) {
  if (dictImpo[key] in newdict) {
    newdict[dictImpo[key]].push(key);
  } else {
    newdict[dictImpo[key]] = [key];
  }
}
console.log(newdict);
