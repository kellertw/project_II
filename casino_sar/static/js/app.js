from data.js;
var tableData = data;
var tbody = d3.select('tbody');
var input = d3.select('input');
var btn = d3.select('button');

renderData(tableData);
btn.on('click', handleClick);

// =========================================
function renderData(data) {
    tbody.html('');

    data.forEach(tableRow => {
        var row = tbody.append('tr');
        Object.values(tableRow).forEach(val => {
            var cell = row.append('td');
            cell.text(val);
        });
    });
};

function handleClick() {
    var date = input.property('value');
    var filteredData = tableData;

    if (date) {
        filteredData = filteredData.filter(row => row.state === date)
    };
    renderData(filteredData);
    input.property('value','');
};
// // Use D3 fetch to read the JSON file
// The data from the JSON file is arbitrarily named importedData as the argument
d3.json("/api/v1.0/fincrimes")
  .then(function(importedData){
  // console.log(importedData);
  var data = importedData;
//   // Sort the data array using the Count value
  data.sort(function(a, b) {
    return parseFloat(b.Count) - parseFloat(a.Count);
  });
//   // Slice the first 10 objects for plotting
  data = data.slice(0, 10);
//   // Reverse the array due to Plotly's defaults
  data = data.reverse();
//   // Trace1 for the SuspiciousActivity Data
  var trace1 = {
    x: data.map(row => row.Count),
    y: data.map(row => row.State),
    text: data.map(row => row.State),
    name: "SuspiciousActivity",
    type: "bar",
    orientation: "h"
  };
//   // data
  var chartData = [trace1];
//   // Apply the group bar mode to the layout
  var layout = {
    title: "SuspiciousActivity gods search results",
    margin: {
      l: 100,
      r: 100,
      t: 100,
      b: 100
    }
  };
  // Render the plot to the div tag with id "plot"
  Plotly.newPlot("plotly", chartData, layout);
});