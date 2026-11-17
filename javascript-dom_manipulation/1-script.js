#!/usr/bin/node
const header = document.querySelector('header');
const redheader = document.getElementById('red_header');

function MakeRed () {
  header.style.color = '#FF0000';
}

redheader.addEventListener('click', MakeRed());
