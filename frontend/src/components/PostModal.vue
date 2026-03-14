<template>
  <Transition name="modal">
    <div v-if="publication" class="modal-overlay" @click.self="$emit('close')">
      <div class="modal-content">
        <button class="modal-close" @click="$emit('close')">&times;</button>
        <h2 class="modal-title">{{ publication.title }}</h2>
        <p class="modal-body">{{ publication.text }}</p>
        <div class="modal-meta">
          <span>{{ formattedDate }}</span>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { Publication } from '../api'

const props = defineProps<{
  publication: Publication | null
}>()

defineEmits<{
  close: []
}>()

const formattedDate = computed(() => {
  if (!props.publication) return ''
  return new Date(props.publication.created_at).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  })
})
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 200;
  padding: 16px;
}

.modal-content {
  background: #fff;
  border-radius: 12px;
  padding: 32px;
  max-width: 600px;
  width: 100%;
  max-height: 80vh;
  overflow-y: auto;
  position: relative;
}

.modal-close {
  position: absolute;
  top: 12px;
  right: 16px;
  background: none;
  border: none;
  font-size: 28px;
  cursor: pointer;
  color: #999;
  line-height: 1;
}

.modal-close:hover {
  color: #333;
}

.modal-title {
  font-size: 24px;
  font-weight: 700;
  color: #1a1a2e;
  margin-bottom: 16px;
  padding-right: 32px;
}

.modal-body {
  font-size: 16px;
  line-height: 1.7;
  color: #444;
  white-space: pre-wrap;
}

.modal-meta {
  margin-top: 24px;
  padding-top: 16px;
  border-top: 1px solid #eee;
  font-size: 13px;
  color: #999;
}

/* Transition */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.25s ease;
}

.modal-enter-active .modal-content,
.modal-leave-active .modal-content {
  transition: transform 0.25s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-content {
  transform: translateY(20px);
}

.modal-leave-to .modal-content {
  transform: translateY(20px);
}
</style>
