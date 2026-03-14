<template>
  <div class="post-card" @click="$emit('click')">
    <h3 class="post-title">{{ publication.title }}</h3>
    <p class="post-content">{{ truncatedContent }}</p>
    <div class="post-meta">
      <span class="post-date">{{ formattedDate }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { Publication } from '../api'

const props = defineProps<{
  publication: Publication
}>()

defineEmits<{
  click: []
}>()

const truncatedContent = computed(() => {
  const text = props.publication.text
  return text.length > 150 ? text.slice(0, 150) + '...' : text
})

const formattedDate = computed(() => {
  return new Date(props.publication.created_at).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  })
})
</script>

<style scoped>
.post-card {
  background: #fff;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 12px;
  cursor: pointer;
  transition: box-shadow 0.2s;
  border: 1px solid #e8e8e8;
}

.post-card:hover {
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
}

.post-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 8px;
  color: #1a1a2e;
}

.post-content {
  font-size: 14px;
  color: #666;
  line-height: 1.5;
  margin-bottom: 12px;
}

.post-meta {
  display: flex;
  justify-content: flex-end;
}

.post-date {
  font-size: 12px;
  color: #999;
}
</style>
