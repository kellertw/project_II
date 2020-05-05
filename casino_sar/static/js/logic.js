// Create a map object
var myMap = L.map("map", {
  center: [33.31, -114.70],
  zoom: 4
});

var street = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets-basic",
  accessToken: API_KEY
}).addTo(myMap);

var mydata=[];
d3.json("http://127.0.0.1:5000/county",function(data){
  data.forEach(function(d) {
        var lat = d.Lat;
        var long = d.Long;
        var name = d.State;
        var industry = d.Industry
        var place={
            latitude:lat,
            longitude:long,
            name:name,
            industry:industry
          }
          var circle = L.marker([place.latitude,place.longitude],{

          }).addTo(myMap);
            circle.bindPopup(place.industry).openPopup();
    //  mydata.push(dictO);
  })

});


