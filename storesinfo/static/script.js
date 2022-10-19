const url = new URL(document.location.href);
const path = url.pathname.replace(/\//g, '');
const nav = document.querySelector('#navItems');

switch (path) {
  case "":
    nav.children[0].classList.add('active')
    break;
  case "locations":
    nav.children[1].classList.add('active')
    locationsMap()
    break;
  case "metrics":
    nav.children[2].classList.add('active')
    break;
  case "charts":
    nav.children[3].classList.add('active')
    break;
  case "populations":
    nav.children[4].classList.add('active')
    populationMaps()
    break;
  case "clusters":
    nav.children[5].classList.add('active')
    clustersMaps()
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
      city: 'Tokyo'
    },
    {
      latitude: 34.6745148,
      longitude: 135.5010324,
      storeName: 'H&M Shinsaibashi',
      city: 'Osaka'
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


function populationMaps(){
  var map1 = L.map('map1').setView([22.824722452136204, 174.73532038186778], 2);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 20,
    attribution: '© OpenStreetMap'
  }).addTo(map1);

  const locations = obtainMarkers();
  var markers1 = L.markerClusterGroup();

  for (a of locations) {
    let dataPopUp = `
<b>${a.storeName}, ${a.city}</b>
<br>
<label>Lat: ${a.latitude}, Lng: ${a.longitude}</label>`

    var marker1 = L.marker([a.latitude, a.longitude]).addTo(map1);
    marker1.bindPopup(dataPopUp).openPopup();
    markers1.addLayer(marker1);
  }

  map1.addLayer(markers1);



  var map2 = L.map('map2').setView([22.824722452136204, 174.73532038186778], 2);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 20,
    attribution: '© OpenStreetMap'
  }).addTo(map2);

  var markers2 = L.markerClusterGroup();

  for (a of locations) {
    let dataPopUp = `
<b>${a.storeName}, ${a.city}</b>
<br>
<label>Lat: ${a.latitude}, Lng: ${a.longitude}</label>`

    var marker2 = L.marker([a.latitude, a.longitude]).addTo(map2);
    marker2.bindPopup(dataPopUp).openPopup();
    markers2.addLayer(marker2);
  }

  map2.addLayer(markers2);




  var map3 = L.map('map3').setView([22.824722452136204, 174.73532038186778], 2);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 20,
    attribution: '© OpenStreetMap'
  }).addTo(map3);

  var markers3 = L.markerClusterGroup();

  for (a of locations) {
    let dataPopUp = `
<b>${a.storeName}, ${a.city}</b>
<br>
<label>Lat: ${a.latitude}, Lng: ${a.longitude}</label>`

    var marker3 = L.marker([a.latitude, a.longitude]).addTo(map3);
    marker3.bindPopup(dataPopUp).openPopup();
    markers3.addLayer(marker3);
  }

  map3.addLayer(markers3);
}
function clustersMaps(){
  var map1 = L.map('map1').setView([22.824722452136204, 174.73532038186778], 2);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 20,
    attribution: '© OpenStreetMap'
  }).addTo(map1);

  const locations = obtainMarkers();
  var markers1 = L.markerClusterGroup();

  for (a of locations) {
    let dataPopUp = `
<b>${a.storeName}, ${a.city}</b>
<br>
<label>Lat: ${a.latitude}, Lng: ${a.longitude}</label>`

    var marker1 = L.marker([a.latitude, a.longitude]).addTo(map1);
    marker1.bindPopup(dataPopUp).openPopup();
    markers1.addLayer(marker1);
  }

  map1.addLayer(markers1);



  var map2 = L.map('map2').setView([22.824722452136204, 174.73532038186778], 2);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 20,
    attribution: '© OpenStreetMap'
  }).addTo(map2);

  var markers2 = L.markerClusterGroup();

  for (a of locations) {
    let dataPopUp = `
<b>${a.storeName}, ${a.city}</b>
<br>
<label>Lat: ${a.latitude}, Lng: ${a.longitude}</label>`

    var marker2 = L.marker([a.latitude, a.longitude]).addTo(map2);
    marker2.bindPopup(dataPopUp).openPopup();
    markers2.addLayer(marker2);
  }

  map2.addLayer(markers2);




  var map3 = L.map('map3').setView([22.824722452136204, 174.73532038186778], 2);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 20,
    attribution: '© OpenStreetMap'
  }).addTo(map3);

  var markers3 = L.markerClusterGroup();

  for (a of locations) {
    let dataPopUp = `
<b>${a.storeName}, ${a.city}</b>
<br>
<label>Lat: ${a.latitude}, Lng: ${a.longitude}</label>`

    var marker3 = L.marker([a.latitude, a.longitude]).addTo(map3);
    marker3.bindPopup(dataPopUp).openPopup();
    markers3.addLayer(marker3);
  }

  map3.addLayer(markers3);
}



function locationsMap(){
  var mainMap = L.map('mainMap').setView([22.824722452136204, 174.73532038186778], 2);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 20,
    attribution: '© OpenStreetMap'
  }).addTo(mainMap);

  const locations = obtainMarkers();
  var markersMainMap = L.markerClusterGroup();

  for (a of locations) {
    let dataPopUp = `
<b>${a.storeName}, ${a.city}</b>
<br>
<label>Lat: ${a.latitude}, Lng: ${a.longitude}</label>`

    var markerMainMap = L.marker([a.latitude, a.longitude]).addTo(mainMap);
    markerMainMap.bindPopup(dataPopUp).openPopup();
    markersMainMap.addLayer(markerMainMap);
  }

  mainMap.addLayer(markersMainMap);
}

if (path == 'populations') {
  
}
