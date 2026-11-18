#!/usr/bin/node

const updateHeader = document.getElementById('update_header');
const header = document.querySelector('header');

updateHeader.addEventListener('click', update);

function update () {
  header.innerHTML = 'New Header!!!';
}
