#!/usr/bin/node
const { argv } = require('node:process');
let i = 0;
while (i !== argv[2]) {
  console.log('C is fun');
  i++;
}
