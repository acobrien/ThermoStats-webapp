<template>
<div class="home">
  <img src="@/assets/images/ThermoStatsLogo.png" alt="ThermoStats Logo" class="logo" />
  <h1>ThermoStats Home</h1>
  <button @click="navigateToDashboard">Dashboard</button>
</div>
</template>

<script>
export default {
  methods: {
    navigateToDashboard() {
      this.$router.push('/dashboard');
    }
  }
}
</script>

<style scoped>
.logo {
  display: block;
  align-content: center;
  max-width: 50%;
  height: auto;
  margin-left: auto;
  margin-right: auto;
}
</style>