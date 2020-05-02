var tbody = d3.select("tbody");
var input = d3.select("input");
var btn = d3.select("button");

fetch("http://localhost:5000/data")
  .then((response) => response.json())
  .then((results) => renderData(results.data))
  .catch((err) => console.error(err));
btn.on("click", handleClick);

// =========================================
function renderData(data) {
  tbody.html("");

  data.forEach((tableRow) => {
    var row = tbody.append("tr");
    Object.values(tableRow).forEach((val) => {
      var cell = row.append("td");
      cell.text(val);
    });
  });
}

function handleClick() {
  var date = input.property("value");
  var filteredData = tableData;

  if (date) {
    filteredData = filteredData.filter((row) => row.state === date);
  }
  renderData(filteredData);
  input.property("value", "");
}
