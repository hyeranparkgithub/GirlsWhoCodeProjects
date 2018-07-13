var map;
var view;
var ourLoc;

function init() {
  ourLoc = ol.proj.fromLonLat([-84.460744, 33.914206]);

  view = new ol.View({
    center: ourLoc,
    zoom: 4
  });

  map = new ol.Map({
       target: 'map',
       layers: [
         new ol.layer.Tile({
           source: new ol.source.OSM()
         })
       ],
       loadTilesWhileAnimating: true,
       view: view
     });

   }

function panHome() {
    view.animate({
      center: ourLoc,
      duration: 2000
    });
  }

function panLocation() {
  var userInput = document.getElementById("countryName").value;
  alert("You entered " + userInput);

  if (userInput == "") {
  alert("You didn't type in a country. Please enter a country name.");
  return;
  }

  var query = "http://restcountries.eu/rest/v2/name/" + userInput;
  query = query.replace(/ /g, "%20");

  countryRequest = new XMLHttpRequest();
  countryRequest.open('GET', query, true);
  countryRequest.onload = processCountryRequest;
  countryRequest.send();


}
function processCountryRequest() {
  console.log("Ready State " + countryRequest.readyState);
  console.log("Status " + countryRequest.status);
  console.log("Response " + countryRequest.responseText);

  if(countryRequest.readyState != 4) {
    return;
  } else if(countryRequest.status != 200) {
    return;
  } else if(countryRequest.responseText == "") {
    return;
  }

  var countryInformation = JSON.parse(countryRequest.responseText);
  var lon = countryInformation[0].latlng[1];
  var lat = countryInformation[0].latlng[0];

  view.animate({
    center: ol.proj.fromLonLat([lon, lat]),
    duration: 2000
  });

}
window.onload = init;
