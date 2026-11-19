#!/usr/bin/node

async function HelloText () {
  const helloElement = document.getElementById('hello');
  const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');

  if (response.ok) {
    const data = response.json();

    helloElement.innerHTML = data.hello;
  }
}

HelloText();
