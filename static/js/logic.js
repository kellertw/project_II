// Create a map object
var myMap = L.map("map", {
  center: [33.31, -114.70],
  zoom: 4
});

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets-basic",
  accessToken: API_KEY
<<<<<<< HEAD:js/logic.js
}).addTo(myMap);

// Create a new marker
// Pass in some initial options, and then add it to the map using the addTo method
var cities = [
  {
    name: "Los Angeles",
    location: [34.0522, -118.2437],
  },
  {
    name: "San Diego", 
    location: [32.7157, -117.1611]
  },
  {
    name: "Las Vegas",
    location: [36.1146, -115.1728],
  },
  {
    name: "Inglewood",
    location: [33.9610, -118.3553],
  },
  {
    name: "Phoenix", 
    location: [33.4483, -112.0740],
  },
  {
    name: "Albuquerque",
    location:[35.1068, -106.6292],
  },
  {
    name: "Livingston", 
    location:[30.71, -94.67],
  },
  {
    name: "Houston",
    location: [29.7604, -95.3698],
  },
  {
    name: "Black Hawk", 
    location: [39.7979, -105.4933],
  },
  {
    name: "Denver",
    location: [39.7420, -104.9915],
  },
  {
    name: "Central City", 
    location:[39.8019, -105.5142]
  },
  {
    name: "Salt Lake City",
    location:[40.7587, -111.8761]
  },
  {
    name: "Cedar City",
    location:[37.6804, -1130617]
  },
  {
    name: "Oklahoma City",
    location:[35.4819, -97.5084]
  },
  {
    name: "Norman", 
    location:[35.2225, -97.4394]
  },
  {
    name: "Cripple Creek",
    location: [38.7416, -105.1746]
  }

]
// var marker = L.marker([36.44, -115.17], {
//   draggable: true,
//   title: "My First Marker"
// }).addTo(myMap);

// Binding a pop-up to our marker
for (var i = 0; i < cities.length; i++){
  L.marker(cities[i].location, {
    draggable: true,
  }).addTo(myMap);
}
marker.bindPopup("Casino City");
||||||| 625748f:js/logic.js
}).addTo(myMap);
=======
}).addTo(myMap);

var csvData;

console.log('Hi!');


d3.csv('./data/SARStats_6.csv', data => {
  csvData = data.splice(0,6);

  var row = d3.select('tbody').append('tr')

  csvData.forEach(obj => {
    var cell = row.append('td');

    console.log(obj);
    

    Object.values(obj).forEach(val => {
      cell.text(val);
    })
  });

})


// Count: "17"
// Countym: "Maricopa County, AZ"
// Industry: "Casino/Card Club - Tribal Authorized Casino"
// State: "Arizona"
// Year Month: "2014 January"
>>>>>>> 6e986390238ecd35e4e5d7245bdcea26aeacd232:static/js/logic.js
