<template>
  <div>

    <button @click="writeAllRaw">Write All Raw Files to Savefile</button>

    <div class="single-file">
      <input
          v-model="filename"
          placeholder="Enter filename (e.g., sensor1.csv)"
          @keyup.enter="writeSingleFile"
      >
      <button @click="writeSingleFile">Write Single File</button>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue';

const filename = ref('');

const writeAllRaw = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/load-all-raw', {
      method: 'POST'
    });
    const result = await response.json();
    console.log('Bulk write result:', result.message);
  }
  catch (error) {
    console.error('Bulk write failed:', error);
  }
};

const writeSingleFile = async () => {
  if (!filename.value) return;

  try {
    const response = await fetch('http://localhost:8000/api/process-file', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ filename: filename.value })
    });
    const result = await response.json();
    console.log('Single file write result:', result.message);
    filename.value = '';  // Clear input after successful write
  }
  catch (error) {
    console.error('Single file write failed:', error);
  }
};
</script>

<style scoped>

</style>