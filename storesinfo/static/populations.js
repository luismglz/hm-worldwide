const form = document.querySelector('#displayPopulation');
const mapDiv = document.querySelector('#mapPopulations');
window.addEventListener('load', () => {
    form.addEventListener('submit', handleForm);
});

function handleForm(e) {
    e.preventDefault();

    //validate
    const id = document.querySelector('#clusterId').value;
    const measurement = document.querySelector('#measurement').value;

    //consult the API
    getCluster(id, Number(measurement));
}

function getCluster(id, measurement) {
    const URL = `http://127.0.0.1:8000/population/${id}/`;

    fetch(URL)
        .then((response) => response.json())
        .then((result) => {
            //removeMap();

            //print result in HTML
            showMap(result, measurement);
        });
}

function showMap(data, measurement) {
    mapDiv.innerHTML = "<div id='map' style='width: 100%; height: 100%;'></div>";
    var map = L.map('map').setView([data[0].lat[1], data[0].lng[1]], 8);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 9,
        attribution:
            '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);

    const markers1 = data;

    let coordinatesPolygon = [];
    data[0].lat.forEach((element, index) => {
        coordinatesPolygon.push([data[0].lng[index], data[0].lat[index]]);
    });


    var markers = L.markerClusterGroup();
    markers1[0].lat.forEach((element, index) => {
        let dataPopUp = `
        <b>${data[0].title}</b>
        <br>
        <label>Lat: ${element}, Lng: ${markers1[0].lng[index]}</label>`


        var marker = L.marker([element, markers1[0].lng[index]]);
        marker.bindPopup(dataPopUp).openPopup();
        markers.addLayer(marker);
    })

    map.addLayer(markers);
    L.Polygon.addInitHook(function () {
        this._latlng = this._bounds.getCenter();
    });

    switch (measurement) {
        case 1:
            createCenterOfMass()
            break;
        case 2:
            createCentroid()
            break;
        case 3:
            createKinks()
            break;
        case 4:
            createPointGrid()
            break
        case 5:
            createClustersKMeans()
            break;
        default:
            break;
    }

    function makeHullPolygon() {
        var coordinates = []
        for (let i = 0; i < data[0].lng.length; i++) {
            coordinates.push([data[0].lng[i], data[0].lat[i]])
        }
        coordinates.push([...coordinates[0]])

        return turf.polygon([hull(coordinates)]);
    }

    function makePolygon() {
        var coordinates = []
        for (let i = 0; i < 5; i++) {
            coordinates.push([data[0].lng[i], data[0].lat[i]])
        }

        coordinates.push([...coordinates[0]])

        return turf.polygon([coordinates]);
    }

    function makeBBox() {

        var minLng = Math.min(...data[0].lng)
        var maxLng = Math.max(...data[0].lng)

        var minLat = Math.min(...data[0].lat)
        var maxLat = Math.max(...data[0].lat)
        console.log(data[0].lng, data[0].lat)
        console.log('minmax', [minLng, minLat, maxLng, maxLat])

        return [minLng, minLat, maxLng, maxLat];
    }

    function createCenterOfMass() {
        try {
            var polygon = makeHullPolygon()
            var centerOfMass = turf.centerOfMass(polygon)
            L.geoJSON(polygon).addTo(map)
            L.geoJSON(centerOfMass).addTo(map)
        } catch (error) {
            console.log(error)
        }
    }

    function createCentroid() {
        var polygon = makeHullPolygon()
        var centroid = turf.centroid(polygon);
        L.geoJSON(polygon).addTo(map)
        L.geoJSON(centroid).addTo(map)
    }

    function createKinks() {
        var polygon = makePolygon()
        var kinks = turf.kinks(polygon);
        L.geoJSON(polygon).addTo(map)
        L.geoJSON(kinks).addTo(map)
    }

    function createPointGrid() {
        var coordinates = []
        for (let i = 0; i < data[0].lng.length; i++) {
            coordinates.push([data[0].lng[i], data[0].lat[i]])
        }
        coordinates.push([...coordinates[0]])


        var extent = makeBBox()
        var cellSide = 30;
        var options = { units: 'miles' };

        var grid = turf.pointGrid(extent, cellSide, options);
        L.geoJSON(grid).addTo(map)
    }

    function createClustersKMeans() {
        var points = turf.randomPoint(100, { bbox: makeBBox() });
        var options = { numberOfClusters: 20 };
        var clustered = turf.clustersKmeans(points, options);
        L.geoJSON(clustered).addTo(map)
    }
}

function removeMap() {
    while (mapDiv.firstChild) {
        mapDiv.className = '';
        mapDiv.removeChild(mapDiv.firstChild);
    }
}
