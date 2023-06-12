
document.addEventListener("DOMContentLoaded", function() {
  const total_heifers = document.getElementById('herd-summary-chart').dataset.total_heifers;

  const total_bulls = document.getElementById('herd-summary-chart').dataset.total_bulls;
  const total_cattle = document.getElementById('herd-summary-chart').dataset.total_cattle;
  const total_preg = document.getElementById('herd-preg-chart').dataset.total_pregnant;


  var ctx = document.getElementById("herd-summary-chart").getContext("2d");
  new Chart(ctx, {
    type: "pie",
    scale : 0.3,
    data: {
      labels: ["Heifers", "Bulls"],
      datasets: [{
        label: "Herd Composition",
        data: [total_heifers, total_bulls], 
        backgroundColor: ["rgba(54, 162, 235, 0.8)", "rgba(255, 99, 132, 0.8)"],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true
    }
  });

  var ctx = document.getElementById("herd-preg-chart").getContext("2d");
  new Chart(ctx, {
    type: "pie",
    scale : 0.3,
    data: {
      labels: ["Not pregnant", "Pregnant"],
      datasets: [{
        label: "Herd pregnant",
        data: [total_heifers, total_preg], 
        backgroundColor: ["rgba(54, 162, 235, 0.8)", "rgba(255, 99, 132, 0.8)"],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true
    }
  });




});
