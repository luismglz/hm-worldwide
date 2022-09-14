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


function obtainMarkers() {
  const places = [
    {
      latitude: 35.6695519365523,
      longitude: 139.705989360809,
      storeName: 'H&M Harajuku',
      city:'Tokyo'
    },
    {
      latitude: 34.6745148,
      longitude: 135.5010324,
      storeName: 'H&M Shinsaibashi',
      city:'Osaka'
    },
    {
      latitude: 37.5634087176005,
      longitude: 126.984644830226,
      storeName: 'Myeongdong Junganggil Store',
      city: 'Seoul'
    },
    {
      latitude: 32.073807,
      longitude: 34.791115,
      storeName: '132 Menachem Begin St',
      city: 'Tel Aviv'
    },
    {
      latitude: 19.67363989039507,
      longitude: -101.16530576,
      storeName: 'Paseo Altozano, Av. Montaña Monarca Norte #1000',
      city: 'Morelia'
    },
    {
      latitude: 6.205892,
      longitude: -75.559087,
      storeName: 'H&M El Tesoro',
      city: 'Medellin'
    },
    {
      latitude: 40.7537936,
      longitude: -74.0018791,
      storeName: 'H&M Hudson Yards',
      city: 'New York City'
    },
    {
      latitude: 34.66219682,
      longitude: -92.40949615,
      storeName: 'H&M Outlets of Little Rock',
      city: 'Little Rock, Arkansas'
    },

  ]
  
  return places;
}

var map = L.map('map').setView([22.824722452136204, 174.73532038186778], 2);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 20,
  attribution: '© OpenStreetMap'
}).addTo(map);

const markers1 = obtainMarkers();

var markers = L.markerClusterGroup();



for (a of markers1) {
  let dataPopUp = `
<b>${a.storeName}, ${a.city}</b>
<br>
<label>Lat: ${a.latitude}, Lng: ${a.longitude}</label>`

  var marker = L.marker([a.latitude, a.longitude]).addTo(map);
  marker.bindPopup(dataPopUp).openPopup();
  markers.addLayer(marker);
}

map.addLayer(markers); 