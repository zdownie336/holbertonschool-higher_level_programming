const theader = document.getElementById('toggle_header');
const header = document.querySelector('header');

function toggles () {
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
}

theader.addEventListener('click', toggles);
