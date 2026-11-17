#!/usr/bin/node
const { argv } = require('node:process');
const number = parseInt(argv[2]);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  const row = [];
  for (let i = number; i > 0; i--) {
    row.push('X');
  }
  for (let i = number; i > 0; i--) {
    console.log(row.join(''));
  }
}
