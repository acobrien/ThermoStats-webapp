<template>
  <body>
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

  <div class="select-and-stats-container">
    <div class="select-container">
      <!-- Thermostat Select -->
      <div class="select-wrapper">
        <select v-model="selectedThermostat" @change="updateDates(); updateStats(); updateCost();">
          <option disabled value="">Thermostat</option>
          <option v-for="option in thermostat_options" :key="option" :value="option">
            {{ option }}
          </option>
        </select>
      </div>

      <!-- Date Select -->
      <div class="select-wrapper">
        <select v-model="selectedDate" @change="updateStats(); updateCost();">
          <option disabled value="">Date</option>
          <option v-for="option in date_options" :key="option" :value="option">
            {{ option }}
          </option>
        </select>
      </div>

      <button @click="navigateToDashboard">Dashboard</button>

      <div v-if="selectedThermostat && selectedDate" class="cost-display">
        <strong>{{ selectedThermostat }} on {{ selectedDate }}: ${{ formattedThermostatDayCost }}</strong>
      </div>
    </div>

    <!-- Statistics Display -->
    <div class="statistics-container">
      <div class="column">
        <div v-for="(sensor, index) in columnOne" :key="index" class="sensor-card">
          <h4>{{ sensor[0] }}</h4>
          <p><strong>Max:</strong> {{ sensor[1] }} ({{ sensor[2] }}°)</p>
          <p><strong>Min:</strong> {{ sensor[3] }} ({{ sensor[4] }}°)</p>
          <p><strong>Avg:</strong> {{ sensor[5].toFixed(2) }}°</p>
        </div>
      </div>
      <div class="column">
        <div v-for="(sensor, index) in columnTwo" :key="index" class="sensor-card">
          <h4>{{ sensor[0] }}</h4>
          <p><strong>Max:</strong> {{ sensor[1] }} ({{ sensor[2] }}°)</p>
          <p><strong>Min:</strong> {{ sensor[3] }} ({{ sensor[4] }}°)</p>
          <p><strong>Avg:</strong> {{ sensor[5].toFixed(2) }}°</p>
        </div>
      </div>
      <div class="column">
        <div v-for="(sensor, index) in columnThree" :key="index" class="sensor-card">
          <h4>{{ sensor[0] }}</h4>
          <p><strong>Max:</strong> {{ sensor[1] }} ({{ sensor[2] }}°)</p>
          <p><strong>Min:</strong> {{ sensor[3] }} ({{ sensor[4] }}°)</p>
          <p><strong>Avg:</strong> {{ sensor[5].toFixed(2) }}°</p>
        </div>
      </div>
    </div>
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
      selectedDate: '',
      thermostat_options: [],
      date_options: [],
      statistics: [],
      thermostatDayCost: '',
    };
  },
  computed: {
    columnOne() {
      return this.statistics.filter((_, index) => index % 3 === 0);
    },
    columnTwo() {
      return this.statistics.filter((_, index) => index % 3 === 1);
    },
    columnThree() {
      return this.statistics.filter((_, index) => index % 3 === 2);
    },
    formattedThermostatDayCost() {
      return Number(this.thermostatDayCost).toFixed(2);
    }
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
    async updateDates() {
      if (!this.selectedThermostat) return;
      const response = await fetch(`http://localhost:8000/api/date_options?thermostat_id=${this.selectedThermostat}`);
      this.date_options = await response.json();
    },
    async updateStats() {
      if (!this.selectedThermostat || !this.selectedDate) return;
      const response = await fetch(`http://localhost:8000/api/get_statistics?thermostat_id=${this.selectedThermostat}&date=${this.selectedDate}`);
      this.statistics = await response.json();
    },
    async updateCost() {
      if (!this.selectedThermostat || !this.selectedDate) return;
      const response = await fetch(`http://localhost:8000/api/thermostat_day_cost?thermostat_id=${this.selectedThermostat}&date=${this.selectedDate}`);
      this.thermostatDayCost = await response.json();
    }
  }
};
</script>

<style scoped>
.charts-container > * {
  max-height: 39vh;
}

.select-and-stats-container {
  display: flex;
  align-items: flex-start;
  gap: 20px;
}

.select-container {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.statistics-container {
  padding: 10px;
  gap: 20px;
  white-space: pre-wrap;
  display: flex;
  flex-grow: 1;
}

.statistics-container {
  display: flex;
  gap: 20px;
}

.column {
  flex: 1;
}

.sensor-card {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
}

.cost-display {
  border: 1px solid #ccc;
  padding: 10px;
}
</style>