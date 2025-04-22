<template>
  <body>
  <div>
    <router-link to="/">
      <img src="@/assets/images/ThermoStatsLogo.png" alt="ThermoStats Logo" class="logo" />
    </router-link>
  </div>
  <div class="charts-container">
    <energy-chart>
      :recorded-temps="recordedTempList"
      :recorded-costs="recordedCostList"
      :interpolated-temps="interpolatedTempList"
      :interpolated-costs="interpolatedCostList"
    </energy-chart>
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
    };
  },
  async created() {
    const [recorded_temps_response, recorded_costs_response,
      interpolated_temps_response, interpolated_costs_response] =
        await Promise.all([
            fetch('http://localhost:8000/api/get_average_temperatures'),
            fetch('http://localhost:8000/api/get_energy_costs'),
            fetch('http://localhost:8000/api/get_interpolated_temperatures'),
            fetch('http://localhost:8000/api/get_interpolated_costs'),
        ]);
    this.recordedTempList = await recorded_temps_response.json();
    this.recordedCostList = await recorded_costs_response.json();
    this.interpolatedTempList = await interpolated_temps_response.json();
    this.interpolatedCostList = await interpolated_costs_response.json();
  }
};
</script>

<style scoped>
.charts-container > * {
  max-height: 39vh;
}
</style>