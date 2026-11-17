#!/usr/bin/node
const header = document.getElementById('red_header');

header.addEventListener('click', MakeRed());
function MakeRed () {

	document.querySelector('header').classList.add('red');
}

