#!/usr/bin/node

const add = document.getElementById('add_item');

add.addEventListener('click', addElement);

function addElement () {
  const list = document.createElement('li');
  list.innerHTML = 'Item';
  document.getElementsByClassName('my_list')[0].appendChild(list);
}
