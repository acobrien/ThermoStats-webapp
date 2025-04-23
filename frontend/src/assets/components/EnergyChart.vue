<template>
  <div class="chart-container">
    <canvas ref="chart"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js'
import { Line } from 'vue-chartjs'

// Register chart components
Chart.register(...registerables)

export default {
  extends: Line,
  props: {
    recordedTemps: Array,
    recordedCosts: Array,
    interpolatedTemps: Array,
    interpolatedCosts: Array
  },
  methods: {
    renderChart() {
      if (
          !this.recordedTemps?.length ||
          !this.recordedCosts?.length ||
          !this.interpolatedTemps?.length ||
          !this.interpolatedCosts?.length
      ) return;

      const chartData = {
        labels: this.interpolatedTemps,
        datasets: [
          {
            label: 'Interpolated Function',
            data: this.interpolatedCosts,
            borderColor: 'coral',
            tension: 0.3,
            fill: false,
            pointRadius: 1.5,
          },
          {
            label: 'Recorded Data',
            data: this.recordedCosts.map((cost, index) => ({
              x: this.recordedTemps[index],
              y: cost
            })),
            borderColor: 'paleturquoise',
            backgroundColor: 'paleturquoise',
            type: 'scatter',
            showLine: false,
            pointRadius: 5,
          }
        ]
      };

      const options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            title: {
              display: true,
              text: 'Temperature'
            }
          },
          y: {
            title: {
              display: true,
              text: 'Energy Cost - $'
            }
          }
        },
        plugins: {
          title: {
            display: true,
            text: 'Average Temperature vs. Daily Energy Cost',
            font: {
              size: 20
            }
          }
        }
      };

      if (this.chart) this.chart.destroy();
      this.chart = new Chart(this.$refs.chart, {
        type: 'scatter',
        data: chartData,
        options: options
      });
    }
  },
  mounted() {
    this.renderChart()
  }
}
</script>

<style>
.chart-container {
  height: 400px;
  position: relative;
}
</style>