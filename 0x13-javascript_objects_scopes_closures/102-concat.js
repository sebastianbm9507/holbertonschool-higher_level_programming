#!/usr/bin/node
const fs = require('fs');

const readData = (ruta) => {
  try {
    return fs.readFileSync(ruta, 'utf-8');
  } catch (err) {
    console.log(err);
  }
};
//  Gathering data 📀
const dataFile1 = readData(process.argv[2]);
const dataFile2 = readData(process.argv[3]);

// Writting file 📂
fs.writeFile(process.argv[4], dataFile1 + dataFile2, (err) => {
  // Catch error with first error callback technique ❗️
  if (err) {
    console.log('An error has occurred');
  }
});
