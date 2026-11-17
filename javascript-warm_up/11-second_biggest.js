#!/usr/bin/node
const { argv } = require('node:process');
const arr = argv.slice(2);

arr.sort((a, b) => b - a);

if (arr.length <= 1) {
  console.log(0);
} else {
  console.log(arr[1]);
}
