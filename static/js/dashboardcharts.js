document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the data attributes from the canvas element
    var canvas = document.getElementById('herd-summary-chart');
    var totalCattle = parseInt(canvas.dataset.totalCattle);
    var totalHeifers = parseInt(canvas.dataset.totalHeifers);
    var totalBulls = parseInt(canvas.dataset.totalBulls);
  
    // Calculate the percentage of bulls and heifers
    var percentageHeifers = (totalHeifers / totalCattle) * 100;
    var percentageBulls = (totalBulls / totalCattle) * 100;
  
    // Create the pie chart
    var chart = new Chart(canvas, {
      type: 'pie',
      data: {
        labels: ['Heifers', 'Bulls'],
        datasets: [{
          label: 'Herd Composition',
          data: [percentageHeifers, percentageBulls],
          backgroundColor: [
            'rgba(54, 162, 235, 0.8)',
            'rgba(255, 99, 132, 0.8)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    });
  });
  