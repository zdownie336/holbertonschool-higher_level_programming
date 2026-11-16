#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] === undefined) {
  console.log('C is undefined');
} else {
  console.log('C is ' + argv[2]);
}
