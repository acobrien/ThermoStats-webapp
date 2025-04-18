<template>
<div class="home">

  <div>
    <img src="@/assets/images/ThermoStatsLogo.png" alt="ThermoStats Logo" class="logo" />
  </div>

  <div class="info">
    <h1>ThermoStats Home</h1>
    <div class="button-group">
      <button @click="navigateToDashboard">Dashboard</button>
      <button @click="navigateToAnalytics">Analytics</button>
    </div>
  </div>

</div>
</template>

<script>
export default {
  methods: {
    navigateToDashboard() {
      this.$router.push('/dashboard');
    },
    navigateToAnalytics() {
      this.$router.push('/analytics');
    }
  }
}
</script>

<style scoped>
.logo {
  display: block;
  align-content: center;
  max-width: 25%;
  height: auto;
  margin: auto;
}

.info {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: auto;
  max-width: 50%;
  text-align: center;
}

.button-group {
  display: flex;
  gap: 10px; /* space between buttons */
  justify-content: center;
}

.button-group button {
  flex: 1;
  min-width: 100px;
}
</style>