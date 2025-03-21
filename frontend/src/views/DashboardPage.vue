<template>
  <div>
    <!-- v-model links textbox with variable -->
    <input v-model="filename" placeholder="filename.txt">

    <!-- calls loadFile() -->
    <button @click="loadFile">Load</button>

    <!-- Display area for file -->
    <pre>{{ content }}</pre>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const filename = ref('');
const content = ref('');

const loadFile = async () => {
  try {
    const response = await fetch(`http://localhost:8000/data/${filename.value}`);
    content.value = await response.text();
  }
  catch (error) {
    console.error('Failed to load file:', error);
  }
};
</script>

<style scoped>

</style>