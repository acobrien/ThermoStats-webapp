<template>
  <div class="select-container">
    <!-- Thermostat Select -->
    <div class="select-wrapper">
      <select v-model="selectedThermostat" @change="updateSensors">
        <option v-for="option in thermostat_options" :key="option" :value="option">
          {{ option }}
        </option>
      </select>
    </div>

    <!-- Sensor Select -->
    <div class="select-wrapper">
      <select v-model="selectedSensor" @change="updateDates">
        <option v-for="option in sensor_options" :key="option" :value="option">
          {{ option }}
        </option>
      </select>
    </div>

    <!-- Date Select -->
    <div class="select-wrapper">
      <select v-model="selectedDate" @change="updateChart">
        <option v-for="option in date_options" :key="option" :value="option">
          {{ option }}
        </option>
      </select>
    </div>
  </div>
  <div>
    <h3>Time List:</h3>
    <div>{{ timeList }}</div>
    <h3>Temperature List:</h3>
    <div>{{ tempList }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedThermostat: '',
      selectedSensor: '',
      selectedDate: '',
      thermostat_options: [],
      sensor_options: [],
      date_options: [],
      timeList: [],
      tempList: [],
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
    async updateSensors() {
      if (!this.selectedThermostat) return;
      this.date_options = [];
      this.selectedSensor = '';
      this.selectedDate = '';
      const response = await fetch(`http://localhost:8000/api/sensor_options?thermostat_id=${this.selectedThermostat}`);
      this.sensor_options = await response.json();
    },
    async updateDates() {
      if (!this.selectedThermostat || !this.selectedSensor) return;
      this.selectedDate = '';
      const response = await fetch(`http://localhost:8000/api/date_options?thermostat_id=${this.selectedThermostat}&sensor_id=${this.selectedSensor}`);
      this.date_options = await response.json();
    },
    async updateChart() {
      if (!this.selectedThermostat || !this.selectedSensor || !this.selectedDate) return;
      const timeResponse = await fetch(`http://localhost:8000/api/time_list?thermostat_id=${this.selectedThermostat}&sensor_id=${this.selectedSensor}&date=${this.selectedDate}`);
      this.timeList = await timeResponse.json();
      const tempResponse = await fetch(`http://localhost:8000/api/temp_list?thermostat_id=${this.selectedThermostat}&sensor_id=${this.selectedSensor}&date=${this.selectedDate}`);
      this.tempList = await tempResponse.json();
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
</style>