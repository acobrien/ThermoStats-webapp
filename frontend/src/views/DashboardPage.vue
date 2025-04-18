<template>
  <body>

    <div class="select-container">
      <!-- Thermostat Select -->
      <div class="select-wrapper">
        <select v-model="selectedThermostat" @change="updateSensors(); updateDates(); updateActivityChart();">
          <option disabled value="">Thermostat</option>
          <option v-for="option in thermostat_options" :key="option" :value="option">
            {{ option }}
          </option>
        </select>
      </div>

      <!-- Sensor Select -->
      <div class="select-wrapper">
        <select v-model="selectedSensor" @change="updateTemperatureChart();">
          <option disabled value="">Sensor</option>
          <option v-for="option in sensor_options" :key="option" :value="option">
            {{ option }}
          </option>
        </select>
      </div>

      <!-- Date Select -->
      <div class="select-wrapper">
        <select v-model="selectedDate" @change="updateTemperatureChart(); updateActivityChart();">
          <option disabled value="">Date</option>
          <option v-for="option in date_options" :key="option" :value="option">
            {{ option }}
          </option>
        </select>
      </div>

      <button @click="navigateToAnalytics">Analytics</button>

    </div>

    <div class="charts-container">
      <activity-chart
          v-if="selectedThermostat && selectedDate"
          :time-list="thermostatTimeList"
          :activity-list="thermostatActivityList"
      ></activity-chart>

      <temperature-chart
          v-if="selectedThermostat && selectedSensor && selectedDate"
          :time-list="sensorTimeList"
          :temp-list="sensorTempList"
      ></temperature-chart>
    </div>
  </body>
</template>

<script>
import TemperatureChart from '../assets/components/TemperatureChart';
import ActivityChart from '../assets/components/ActivityChart.vue';

export default {
  components: {
    TemperatureChart,
    ActivityChart
  },
  data() {
    return {
      selectedThermostat: '',
      selectedSensor: '',
      selectedDate: '',
      thermostat_options: [],
      sensor_options: [],
      date_options: [],
      sensorTimeList: [],
      sensorTempList: [],
      thermostatTimeList: [],
      thermostatActivityList: []
    };
  },
  async created() {
    const [thermostat_response] = await Promise.all([
      fetch('http://localhost:8000/api/thermostat_options')
    ]);

    this.thermostat_options = await thermostat_response.json();
    this.date_options = [];
    this.sensor_options = [];
  },
  methods: {
    navigateToAnalytics() {
      this.$router.push('/analytics');
    },
    async updateSensors() {
      if (!this.selectedThermostat) return;
      this.date_options = [];
      this.selectedSensor = '';
      const response = await fetch(`http://localhost:8000/api/sensor_options?thermostat_id=${this.selectedThermostat}`);
      this.sensor_options = await response.json();
    },
    async updateDates() {
      if (!this.selectedThermostat) return;
      const response = await fetch(`http://localhost:8000/api/date_options?thermostat_id=${this.selectedThermostat}`);
      this.date_options = await response.json();
    },
    async updateTemperatureChart() {
      if (!this.selectedThermostat || !this.selectedSensor || !this.selectedDate) return;
      const timeResponse = await fetch(`http://localhost:8000/api/sensor_time_list?thermostat_id=${this.selectedThermostat}&sensor_id=${this.selectedSensor}&date=${this.selectedDate}`);
      this.sensorTimeList = await timeResponse.json();
      const tempResponse = await fetch(`http://localhost:8000/api/sensor_temp_list?thermostat_id=${this.selectedThermostat}&sensor_id=${this.selectedSensor}&date=${this.selectedDate}`);
      this.sensorTempList = await tempResponse.json();
    },
    async updateActivityChart() {
      if (!this.selectedThermostat || !this.selectedDate) return;
      const timeResponse = await fetch(`http://localhost:8000/api/thermostat_time_list?thermostat_id=${this.selectedThermostat}&date=${this.selectedDate}`);
      this.thermostatTimeList = await timeResponse.json();
      const activityResponse = await fetch(`http://localhost:8000/api/thermostat_activity_list?thermostat_id=${this.selectedThermostat}&date=${this.selectedDate}`)
      this.thermostatActivityList = await activityResponse.json();
    }
  }
};
</script>

<style scoped>
.select-container {
  display: flex;
  gap: 20px;
}

.select-wrapper {
  flex: 1;
}

select {
  width: 100%;
  padding: 8px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

.charts-container {
  max-height: 90vh
}

.charts-container > * {
  max-height: 39vh;
}
</style>