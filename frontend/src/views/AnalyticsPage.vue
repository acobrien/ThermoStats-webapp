<template>
  <body>
  <div>
    <router-link to="/">
      <img src="@/assets/images/ThermoStatsLogo.png" alt="ThermoStats Logo" class="logo" />
    </router-link>
  </div>
  <div class="charts-container">
    <energy-chart
        v-if="recordedTempList.length && recordedCostList.length &&
        interpolatedTempList.length && interpolatedCostList.length"
        :recorded-temps="recordedTempList"
        :recorded-costs="recordedCostList"
        :interpolated-temps="interpolatedTempList"
        :interpolated-costs="interpolatedCostList">
    </energy-chart>
  </div>

  <div class="select-container">
    <!-- Thermostat Select -->
    <div class="select-wrapper">
      <select v-model="selectedThermostat" @change="updateSensors(); updateDates();">
        <option disabled value="">Thermostat</option>
        <option v-for="option in thermostat_options" :key="option" :value="option">
          {{ option }}
        </option>
      </select>
    </div>

    <!-- Sensor Select -->
    <div class="select-wrapper">
      <select v-model="selectedSensor">
        <option disabled value="">Sensor</option>
        <option v-for="option in sensor_options" :key="option" :value="option">
          {{ option }}
        </option>
      </select>
    </div>

    <!-- Date Select -->
    <div class="select-wrapper">
      <select v-model="selectedDate">
        <option disabled value="">Date</option>
        <option v-for="option in date_options" :key="option" :value="option">
          {{ option }}
        </option>
      </select>
    </div>

    <button @click="navigateToDashboard">Dashboard</button>

  </div>

  </body>
</template>

<script>
import EnergyChart from "../assets/components/EnergyChart.vue";

export default {
  components: {
    EnergyChart
  },
  data() {
    return {
      recordedTempList: [],
      recordedCostList: [],
      interpolatedTempList: [],
      interpolatedCostList: [],
      selectedThermostat: '',
      selectedSensor: '',
      selectedDate: '',
      thermostat_options: [],
      sensor_options: [],
      date_options: [],
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const [
          recorded_temps_response,
          recorded_costs_response,
          interpolated_temps_response,
          interpolated_costs_response,
          thermostat_options_response,
        ] = await Promise.all([
          fetch('http://localhost:8000/api/get_average_temperatures'),
          fetch('http://localhost:8000/api/get_energy_costs'),
          fetch('http://localhost:8000/api/get_interpolated_temperatures'),
          fetch('http://localhost:8000/api/get_interpolated_costs'),
          fetch('http://localhost:8000/api/thermostat_options'),
        ]);

        this.recordedTempList = await recorded_temps_response.json();
        this.recordedCostList = await recorded_costs_response.json();
        this.interpolatedTempList = await interpolated_temps_response.json();
        this.interpolatedCostList = await interpolated_costs_response.json();
        this.thermostat_options = await thermostat_options_response.json();
      }
      catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    navigateToDashboard() {
      this.$router.push('/dashboard');
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
  }
};
</script>

<style scoped>
.charts-container > * {
  max-height: 39vh;
}
</style>