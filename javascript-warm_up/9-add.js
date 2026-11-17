#!/usr/bin/node
const {argv} = require('node:process');

function add(a, b){
	const num1 = parseInt(a);
	const num2 = parseInt(b);

	if (isNaN(num1) || isNaN(num2)){
		return NaN;
	}
	else{
		return num1 + num2;
	}
}

console.log(add(argv[2], argv[3]));
