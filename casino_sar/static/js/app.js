from data.js
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
// =========================================
// Create Suspicious Activity Stacked Bar Chart
var activity1 = {
    x: ['Arizona', 'California', 'Colorado',
        'New Mexico', 'Nevada','Utah'],
    y: [2, 5, 5, 7, 9, 3],
    name: 'Structuring',
    type: 'bar'
  };
  
  var activity2 = {
    x: ['Arizona', 'California', 'Colorado',
        'New Mexico', 'Nevada','Utah'],
    y: [12, 18, 29, 21, 15, 13],
    name: 'Counting Cards',
    type: 'bar'
  };
  
  var activity3 = {
    x: ['Arizona', 'California', 'Colorado',
        'New Mexico', 'Nevada','Utah'],
    y: [10, 8, 9, 6, 14, 12],
    name: 'Chip Walking',
    type: 'bar'
  };

  var activity4 = {
    x:  ['Arizona', 'California', 'Colorado',
         'New Mexico', 'Nevada','Utah'],
    y: [12, 18, 29, 23, 8, 14],
    name: 'Intra-Casino Funds Transfers',
    type: 'bar'
  };

  var activity5 = {
    x:  ['Arizona', 'California', 'Colorado',
         'New Mexico', 'Nevada','Utah'],
    y: [12, 18, 29, 12, 19, 23],
    name: 'Source of Chips',
    type: 'bar'
  };

  var data = [activity1, activity2, activity3,
            activity4, activity5];
  
  var layout = {barmode: 'stack'};
  
  Plotly.newPlot("plotly", data, layout);