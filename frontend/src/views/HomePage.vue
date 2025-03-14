<template>
<div class="home">
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

</style>