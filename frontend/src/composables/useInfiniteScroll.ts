import { onMounted, onUnmounted, ref } from 'vue'

export function useInfiniteScroll(callback: () => void, threshold = 500) {
  const loading = ref(false)

  const handleScroll = () => {
    const scrollHeight = document.documentElement.scrollHeight
    const scrollTop = document.documentElement.scrollTop
    const clientHeight = document.documentElement.clientHeight

    if (scrollHeight - scrollTop - clientHeight < threshold && !loading.value) {
      loading.value = true
      callback()
    }
  }

  const done = () => {
    loading.value = false
  }

  onMounted(() => window.addEventListener('scroll', handleScroll))
  onUnmounted(() => window.removeEventListener('scroll', handleScroll))

  return { loading, done }
}
