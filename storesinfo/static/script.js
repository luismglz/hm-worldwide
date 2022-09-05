const url = new URL(document.location.href);
const path = url.pathname.replace(/\//g, '');
const nav = document.querySelector('#navItems');

switch (path) {
  case "":
    nav.children[0].classList.add('active')
    break;
  case "locations":
    nav.children[1].classList.add('active')
    break;
  case "metrics":
    nav.children[2].classList.add('active')
    break;
  case "charts":
    nav.children[3].classList.add('active')
    break;
  default:
    break;
}