import { createApp } from 'vue';
import { Pie, reactiveProp } from 'vue-chartjs';

const app = createApp({});

app.component('herd-summary-chart', {
extends: Pie,
props: ['chartData', 'options'],
mixins: [reactiveProp],
mounted() {
this.renderChart(this.chartData, this.options);
},
});

// Data for the chart
const chartData = {
labels: ['Heifers', 'Bulls', 'Calves'],
datasets: [
{
label: 'Herd Composition',
data: [50, 30, 20], // Example data, replace with actual values
backgroundColor: ['rgba(54, 162, 235, 0.8)', 'rgba(255, 99, 132, 0.8)', 'rgba(255, 205, 86, 0.8)'],
borderWidth: 1,
},
],
};

// Options for the chart
const chartOptions = {
responsive: true,
maintainAspectRatio: false,
};

// Mount the app and pass the chart data and options as props
app.mount('#app', {
data() {
return {
chartData: chartData,
chartOptions: chartOptions,
};
},
});