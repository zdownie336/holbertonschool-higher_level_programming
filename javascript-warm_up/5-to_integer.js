#!/usr/bin/node
let {argv} = require('node:process');
let number = parseInt(argv[2])
if (isNaN(number)){
	console.log('Not a number')
}
else {
	console.log('My number: ' + argv[2])
}

