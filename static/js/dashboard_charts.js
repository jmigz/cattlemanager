
// document.addEventListener("DOMContentLoaded", function() {
//   const total_heifers = document.getElementById('herd-summary-chart').dataset.total_heifers;

//   const total_bulls = document.getElementById('herd-summary-chart').dataset.total_bulls;
//   const total_cattle = document.getElementById('herd-summary-chart').dataset.total_cattle;
//   const total_preg = document.getElementById('herd-preg-chart').dataset.total_pregnant;


//   var ctx = document.getElementById("herd-summary-chart").getContext("2d");
//   new Chart(ctx, {
//     type: "pie",
//     scale : 0.3,
//     data: {
//       labels: ["Heifers", "Bulls"],
//       datasets: [{
//         label: "Herd Composition",
//         data: [total_heifers, total_bulls], 
//         backgroundColor: ["rgba(54, 162, 235, 0.8)", "rgba(255, 99, 132, 0.8)"],
//         borderWidth: 1
//       }]
//     },
//     options: {
//       responsive: true,
//       maintainAspectRatio: true
//     }
//   });

//   var ctx = document.getElementById("herd-preg-chart").getContext("2d");
//   new Chart(ctx, {
//     type: "pie",
//     scale : 0.3,
//     data: {
//       labels: ["Not pregnant", "Pregnant"],
//       datasets: [{
//         label: "Herd pregnant",
//         data: [total_heifers, total_preg], 
//         backgroundColor: ["rgba(54, 162, 235, 0.8)", "rgba(255, 99, 132, 0.8)"],
//         borderWidth: 1
//       }]
//     },
//     options: {
//       responsive: true,
//       maintainAspectRatio: true
//     }
//   });




// });

google.charts.load('current', { 'packages': ['corechart'] });
google.charts.setOnLoadCallback(function() {drawChart();drawChartpreg();});


function drawChart() {
  var totalHeifers = parseInt(document.getElementById('herd-summary').getAttribute('data-total_heifers'), 10);
  var totalBulls = parseInt(document.getElementById('herd-summary').getAttribute('data-total_bulls'), 10);

  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Category');
  data.addColumn('number', 'Count');
  data.addRows([
    ['Heifers', totalHeifers],
    ['Bulls', totalBulls]
  ]);

  var options = {
    title: 'Herd Composition',
    backgroundColor: {
      fill: 'transparent'
    }
  };

  var chart = new google.visualization.PieChart(document.getElementById('herd-summary'));
  chart.draw(data, options);
}

// Draw the % pregnant chart
function drawChartpreg() {
  var totalHeifers = parseInt(document.getElementById('herd-preg-chart').getAttribute('data-total_heifers'), 10);
  var totalPreg = parseInt(document.getElementById('herd-preg-chart').getAttribute('data-total_pregnant'), 10);

  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Category');
  data.addColumn('number', 'Count');
  data.addRows([
    ['Not Pregnant', totalHeifers],
    ['Pregnant', totalPreg]
  ]);

  var options = {
    title: 'Herd Pregnancy Stats',
    backgroundColor: {
      fill: 'transparent'
    },
    legend: {position: 'bottom', textStyle: {color: 'blue', fontSize: '0.8em' }},
    
    pieSliceText: 'label',
    

  };

  var chart = new google.visualization.PieChart(document.getElementById('herd-preg-chart'));
  chart.draw(data, options);
}
