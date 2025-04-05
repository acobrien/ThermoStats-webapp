<template>
  <div class="select-container">
    <!-- Thermostat Select -->
    <div class="select-wrapper">
      <select v-model="selectedOption1">
        <option v-for="option in options1" :key="option" :value="option">
          {{ option }}
        </option>
      </select>
    </div>

    <!-- Sensor Select -->
    <div class="select-wrapper">
      <select v-model="selectedOption2">
        <option v-for="option in options2" :key="option" :value="option">
          {{ option }}
        </option>
      </select>
    </div>

    <!-- Date Select -->
    <div class="select-wrapper">
      <select v-model="selectedOption3">
        <option v-for="option in options3" :key="option" :value="option">
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
      options1: [],
      options2: [],
      options3: [],
    };
  },
  async created() {
    const [response1, response2, response3] = await Promise.all([
      fetch('http://localhost:8000/api/thermostat_options'),
      fetch('http://localhost:8000/api/sensor_options'),
      fetch('http://localhost:8000/api/date_options'),
    ]);

    this.options1 = await response1.json();
    this.options2 = await response2.json();
    this.options3 = await response3.json();
  },
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