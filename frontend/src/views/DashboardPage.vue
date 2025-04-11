<template>
  <div class="select-container">
    <!-- Thermostat Select -->
    <div class="select-wrapper">
      <select v-model="selectedOption1" @change="updateSensors">
        <option v-for="option in thermostat_options" :key="option" :value="option">
          {{ option }}
        </option>
      </select>
    </div>

    <!-- Sensor Select -->
    <div class="select-wrapper">
      <select v-model="selectedOption2" @change="updateDates">
        <option v-for="option in sensor_options" :key="option" :value="option">
          {{ option }}
        </option>
      </select>
    </div>

    <!-- Date Select -->
    <div class="select-wrapper">
      <select v-model="selectedOption3">
        <option v-for="option in date_options" :key="option" :value="option">
          {{ option }}
        </option>
      </select>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedOption1: '',
      selectedOption2: '',
      selectedOption3: '',
      thermostat_options: [],
      sensor_options: [],
      date_options: [],
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
      if (!this.selectedOption1) return;
      this.date_options = [];
      this.selectedOption2 = '';
      this.selectedOption3 = '';
      const response = await fetch(`http://localhost:8000/api/sensor_options?thermostat_id=${this.selectedOption1}`);
      this.sensor_options = await response.json();
    },
    async updateDates() {
      if (!this.selectedOption1 || !this.selectedOption2) return;
      this.selectedOption3 = '';
      const response = await fetch(`http://localhost:8000/api/date_options?thermostat_id=${this.selectedOption1}&sensor_id=${this.selectedOption2}`);
      this.date_options = await response.json();
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