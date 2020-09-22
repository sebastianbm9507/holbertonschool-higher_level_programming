#!/usr/bin/node
const request = require('request');

const URL = 'https://swapi-api.hbtn.io/api/films/';
const ID = 18;
var ocurrences = 0;
request(URL, (req, res, body) => {
  const data = JSON.parse(body).results;
  data.forEach(item => {
    const characters = item.characters;
    characters.filter(item => {
      if (item.includes(ID)) ocurrences++;
    }); // end filter 🔚
  }); // end for each 🔚
  console.log(ocurrences);
}); // end request 🔚
