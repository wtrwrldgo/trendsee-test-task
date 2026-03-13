<template>
  <div id="app">
    <nav v-if="showNavbar" class="navbar">
      <router-link to="/" class="nav-brand">Trendsee</router-link>
      <div class="nav-links">
        <router-link to="/">Feed</router-link>
        <router-link to="/video-cart">Video Cart</router-link>
        <router-link to="/analysis">Analysis</router-link>
      </div>
    </nav>
    <main :class="{ 'main-content': showNavbar }">
      <router-view />
    </main>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const showNavbar = computed(() => {
  return route.path !== '/video-cart'
})
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #f5f5f5;
  color: #333;
}

.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  height: 56px;
  background: #fff;
  border-bottom: 1px solid #e0e0e0;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-brand {
  font-size: 20px;
  font-weight: 700;
  color: #1a1a2e;
  text-decoration: none;
}

.nav-links {
  display: flex;
  gap: 16px;
}

.nav-links a {
  text-decoration: none;
  color: #666;
  font-size: 14px;
  padding: 6px 12px;
  border-radius: 6px;
  transition: all 0.2s;
}

.nav-links a:hover,
.nav-links a.router-link-active {
  color: #1a1a2e;
  background: #f0f0f0;
}

.main-content {
  max-width: 800px;
  margin: 24px auto;
  padding: 0 16px;
}
</style>
