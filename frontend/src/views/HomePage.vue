<template>
<div class="home">
  <img src="@/assets/images/ThermoStatsLogo.png" alt="ThermoStats Logo" class="logo" />
  <h1>ThermoStats Home</h1>
  <button @click="navigateToLogin">Sign In</button>
</div>
</template>

<script>
export default {
  methods: {
    navigateToLogin() {
      this.$router.push('/login')
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