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
    timeList: Array,
    activityList: Array
  },
  watch: {
    timeList: {
      handler() {
        this.renderChart()
      },
      deep: true
    },
    activityList: {
      handler() {
        this.renderChart()
      },
      deep: true
    }
  },
  methods: {
    renderChart() {
      if (!this.timeList?.length || !this.activityList?.length) return

      const chartData = {
        labels: this.timeList,
        datasets: [{
          label: 'Activity',
          data: this.activityList,
          borderColor: 'crimson',
          tension: 0.3,
          fill: false
        }]
      }

      const options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            title: {
              display: true,
              text: 'Time'
            }
          },
          y: {
            title: {
              display: true,
              text: 'State'
            }
          }
        }
      }

      // Destroy existing chart before re-rendering
      if (this.chart) this.chart.destroy()
      this.chart = new Chart(this.$refs.chart, {
        type: 'line',
        data: chartData,
        options: options
      })
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