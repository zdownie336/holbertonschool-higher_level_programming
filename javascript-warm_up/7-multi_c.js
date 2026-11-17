#!/usr/bin/node
const { argv } = require('node:process');
let i = parseInt(argv[2]);
while (i > 0) {
  console.log('C is fun');
  i = i - 1;
}
