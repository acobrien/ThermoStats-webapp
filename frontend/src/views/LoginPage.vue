<template>
  <div class="login">
    <h1>ThermoStats Login</h1>
    <form @submit.prevent="handleSubmit">
      <div>
        <label>Username:</label>
        <input type="text" v-model="username">
      </div>
      <div>
        <label>Password:</label>
        <input type="password" v-model="password">
      </div>
      <button type="submit">Login</button>
    </form>
    <p v-if="statusMessage">{{ statusMessage }}</p>
    <router-link to="/">Back to Home</router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "Frontend is running!"
    }
  }
}
</script>