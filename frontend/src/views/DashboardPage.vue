<template>
  <div>
    <select v-model="selectedOptions" multiple>
      <option v-for="option in options" :key="option" :value="option">
        {{ option }}
      </option>
    </select>
    <p>Selected: {{ selectedOptions }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      options: [],
      selectedOptions: []
    }
  },
  async created() {
    const response = await fetch('http://localhost:8000/api/options')
    this.options = await response.json()
  }
}
</script>

<style scoped>

</style>