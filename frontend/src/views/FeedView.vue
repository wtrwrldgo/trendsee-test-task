<template>
  <div class="feed">
    <div class="feed-header">
      <h1>Publications Feed</h1>
      <div class="feed-controls">
        <input
          v-model="userIdInput"
          type="number"
          placeholder="User ID"
          class="input"
        />
        <button class="btn" @click="loadFeed">Load</button>
      </div>
    </div>

    <div v-if="error" class="error">{{ error }}</div>

    <div v-if="publications.length === 0 && !isLoading" class="empty">
      Enter a User ID and click Load to see publications.
    </div>

    <PostCard
      v-for="pub in publications"
      :key="pub.id"
      :publication="pub"
      @click="selectedPost = pub"
    />

    <LoadingSpinner v-if="isLoading" />

    <PostModal :publication="selectedPost" @close="selectedPost = null" />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { getUserPublications, type Publication } from '../api'
import { useInfiniteScroll } from '../composables/useInfiniteScroll'
import LoadingSpinner from '../components/LoadingSpinner.vue'
import PostCard from '../components/PostCard.vue'
import PostModal from '../components/PostModal.vue'

const userIdInput = ref<number | undefined>()
const publications = ref<Publication[]>([])
const selectedPost = ref<Publication | null>(null)
const isLoading = ref(false)
const error = ref('')
const total = ref(0)
const limit = 10

const { done } = useInfiniteScroll(loadMore)

function loadFeed() {
  if (!userIdInput.value) return
  publications.value = []
  total.value = 0
  error.value = ''
  fetchPublications(0)
}

async function loadMore() {
  if (!userIdInput.value) {
    done()
    return
  }
  if (publications.value.length >= total.value && total.value > 0) {
    done()
    return
  }
  await fetchPublications(publications.value.length)
}

async function fetchPublications(offset: number) {
  if (!userIdInput.value || isLoading.value) {
    done()
    return
  }
  isLoading.value = true
  error.value = ''
  try {
    const { data } = await getUserPublications(userIdInput.value, limit, offset)
    if (offset === 0) {
      publications.value = data.items
    } else {
      publications.value.push(...data.items)
    }
    total.value = data.total
  } catch (e: any) {
    error.value = e.response?.data?.detail || 'Failed to load publications'
  } finally {
    isLoading.value = false
    done()
  }
}
</script>

<style scoped>
.feed-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.feed-header h1 {
  font-size: 24px;
  color: #1a1a2e;
}

.feed-controls {
  display: flex;
  gap: 8px;
}

.input {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
  width: 100px;
}

.btn {
  padding: 8px 16px;
  background: #1a1a2e;
  color: #fff;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  cursor: pointer;
}

.btn:hover {
  background: #2a2a4e;
}

.error {
  background: #fee;
  color: #c00;
  padding: 12px;
  border-radius: 6px;
  margin-bottom: 16px;
  font-size: 14px;
}

.empty {
  text-align: center;
  color: #999;
  padding: 48px 0;
  font-size: 16px;
}
</style>
