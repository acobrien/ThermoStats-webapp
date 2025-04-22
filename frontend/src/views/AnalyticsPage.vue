<template>
  <body>
  <div>
    <router-link to="/">
      <img src="@/assets/images/ThermoStatsLogo.png" alt="ThermoStats Logo" class="logo" />
    </router-link>
  </div>
  <energy-chart></energy-chart>
  </body>
</template>

<script setup>

import EnergyChart from "@/assets/components/EnergyChart.vue";
</script>

<style scoped>

</style>