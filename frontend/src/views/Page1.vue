<template>
  <div class="page-layout">
    <!-- Sidebar -->
    <aside class="sidebar">
      <div class="sidebar-logo">
        <img src="/logo.png" alt="trendsee" class="logo-img" />
      </div>

      <div class="sidebar-section">
        <div class="section-label">Поиск контента</div>
        <nav class="sidebar-nav">
          <a href="#" class="nav-item active">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><path d="M3 3h6v6H3V3zm8 0h6v6h-6V3zm-8 8h6v6H3v-6zm8 0h6v6h-6v-6z" stroke="currentColor" stroke-width="1.5"/></svg>
            <span>Главная</span>
          </a>
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><rect x="3" y="3" width="14" height="14" rx="2" stroke="currentColor" stroke-width="1.5"/><polygon points="8,6 8,14 14,10" fill="currentColor"/></svg>
            <span>Видео</span>
          </a>
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="7" stroke="currentColor" stroke-width="1.5"/><circle cx="10" cy="10" r="2.5" fill="currentColor"/></svg>
            <span>Шпионаж</span>
          </a>
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="7" stroke="currentColor" stroke-width="1.5"/><path d="M10 5v5.5l3.5 2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            <span>Контент радар</span>
            <span class="nav-badge">712</span>
          </a>
        </nav>
      </div>

      <div class="sidebar-section">
        <div class="section-label">Работа с соцсетями</div>
        <nav class="sidebar-nav">
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><circle cx="5" cy="10" r="2" stroke="currentColor" stroke-width="1.5"/><circle cx="15" cy="5" r="2" stroke="currentColor" stroke-width="1.5"/><circle cx="15" cy="15" r="2" stroke="currentColor" stroke-width="1.5"/><path d="M7 9l6-3M7 11l6 3" stroke="currentColor" stroke-width="1.5"/></svg>
            <span>Кросс-постинг</span>
          </a>
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><rect x="2" y="4" width="16" height="12" rx="2" stroke="currentColor" stroke-width="1.5"/><path d="M6 9h8M6 12h5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            <span>Чат боты</span>
          </a>
        </nav>
      </div>

      <div class="sidebar-section">
        <div class="section-label">Инструменты</div>
        <nav class="sidebar-nav">
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><path d="M4 16l3-7 3 4 2.5-3.5L16 16H4z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><circle cx="14" cy="6" r="2" stroke="currentColor" stroke-width="1.5"/></svg>
            <span>АИ-сценарий</span>
          </a>
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><rect x="2" y="2" width="16" height="16" rx="2" stroke="currentColor" stroke-width="1.5"/><rect x="5" y="5" width="10" height="10" rx="1" stroke="currentColor" stroke-width="1"/></svg>
            <span>Карусели</span>
          </a>
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><path d="M10 4v12M4 10h12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><circle cx="10" cy="10" r="7" stroke="currentColor" stroke-width="1.5"/></svg>
            <span>Анализ видео</span>
          </a>
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="7" r="3.5" stroke="currentColor" stroke-width="1.5"/><path d="M3 18c0-3.9 3.1-7 7-7s7 3.1 7 7" stroke="currentColor" stroke-width="1.5"/></svg>
            <span>Анализ профиля</span>
          </a>
          <a href="#" class="nav-item disabled">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><rect x="3" y="3" width="14" height="14" rx="2" stroke="currentColor" stroke-width="1.5"/><path d="M7 10h6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            <span>Черновик</span>
            <span class="nav-soon">Скоро</span>
          </a>
        </nav>
      </div>

      <div class="sidebar-bottom">
        <div class="token-bar">
          <span class="token-icon">🔥</span>
          <span class="token-label">Токены</span>
          <span class="token-count">1 245 / 4 497</span>
        </div>
        <div class="token-progress">
          <div class="token-progress-fill" style="width: 27.7%"></div>
        </div>

        <div class="creative-plus">
          <span>Creative +</span>
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M6 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
        </div>

        <div class="sidebar-user">
          <div class="user-avatar">
            <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Alexandra" alt="" />
          </div>
          <div class="user-info">
            <div class="user-name">Александра</div>
            <div class="user-phone">+7 (999) 999-99-99</div>
          </div>
          <svg class="logout-icon" width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M8 3H5a2 2 0 00-2 2v10a2 2 0 002 2h3M13 14l4-4-4-4M17 10H8" stroke="#999" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>

        <div class="lang-selector">
          <span class="lang-flag">🇷🇺</span>
          <span>RU</span>
          <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M3 5l3 3 3-3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
        </div>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="main-content">
      <div class="video-grid">
        <div v-for="card in cards" :key="card.id" class="video-card">
          <!-- Video Thumbnail -->
          <div class="card-thumbnail">
            <div class="thumb-top">
              <div class="reels-badge">
                <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><rect width="12" height="12" rx="3" fill="white" fill-opacity="0.3"/><rect x="2" y="4" width="3" height="4" fill="white"/><rect x="6" y="2" width="4" height="8" fill="white" fill-opacity="0.6"/></svg>
                Reels
              </div>
              <svg class="thumb-heart" width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 21C12 21 3 13.5 3 8.5C3 5.42 5.42 3 8.5 3C10.24 3 11.91 3.81 12 5C12.09 3.81 13.76 3 15.5 3C18.58 3 21 5.42 21 8.5C21 13.5 12 21 12 21Z" stroke="white" stroke-width="1.5"/></svg>
            </div>
            <div class="thumb-badges">
              <span class="x10-badge">X10</span>
            </div>
            <div class="thumb-bottom-right">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M4 16l4-4m0 0l4-4m-4 4l4 4m-4-4L4 8" stroke="white" stroke-width="1.5" stroke-linecap="round"/></svg>
            </div>
            <img :src="card.thumb" :alt="card.author" class="thumb-img" />
            <!-- Overlay text for specific cards -->
            <div v-if="card.overlayText" class="thumb-overlay-text">
              <div class="overlay-en">{{ card.overlayEn }}</div>
              <div class="overlay-ru">{{ card.overlayText }}</div>
            </div>
          </div>

          <!-- Stats Bar -->
          <div class="stats-bar">
            <div class="stat">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="5" stroke="white" stroke-width="1.2"/><circle cx="8" cy="8" r="2" fill="white"/></svg>
              <span>{{ card.views }}</span>
            </div>
            <div class="stat">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 14s-5-3.5-5-7a3.5 3.5 0 017 0 3.5 3.5 0 017 0c0 3.5-5 7-5 7z" stroke="white" stroke-width="1.2"/></svg>
              <span>{{ card.likes }}</span>
            </div>
            <div class="stat">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 4h10a1 1 0 011 1v6a1 1 0 01-1 1H6l-3 2V5a1 1 0 011-1z" stroke="white" stroke-width="1.2"/></svg>
              <span>{{ card.comments }}</span>
            </div>
            <div class="stat">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M4 12l4-4 4 4M4 8l4-4 4 4" stroke="white" stroke-width="1.2" stroke-linecap="round"/></svg>
              <span>{{ card.shares }}</span>
            </div>
          </div>

          <!-- Card Info -->
          <div class="card-info">
            <div class="card-author">
              <div class="author-avatar" :style="{ background: card.avatarBg }"></div>
              <div class="author-details">
                <span class="author-name">{{ card.author }}</span>
                <span class="author-subs">{{ card.subs }}</span>
              </div>
              <div class="author-actions">
                <svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9 3v12M3 9h12" stroke="#999" stroke-width="1.5" stroke-linecap="round"/></svg>
              </div>
            </div>
            <p class="card-text">{{ card.text }}</p>
            <div class="card-date">{{ card.date }}</div>
            <button class="card-btn">Анализ</button>
          </div>
        </div>
      </div>

      <!-- Load More -->
      <div class="load-more-area">
        <button class="load-more-btn">
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9 2l3 5H6l3-5zM6 11h6l-3 5-3-5z" fill="white"/></svg>
          Найти еще ролики
        </button>
        <div class="video-counter">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="8" stroke="#6C5CE7" stroke-width="2" stroke-dasharray="50.26 50.26" stroke-dashoffset="46" stroke-linecap="round" transform="rotate(-90 10 10)"/></svg>
          Видео: 24 из 3000
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
// Thumbnail images — real portrait-style video thumbnails
const thumbs = {
  man: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&h=560&fit=crop&crop=face',
  woman1: 'https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?w=400&h=560&fit=crop&crop=face',
  woman2: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400&h=560&fit=crop&crop=face',
  woman3: 'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=400&h=560&fit=crop&crop=face',
}

const cards = [
  {
    id: 1,
    thumb: thumbs.man,
    views: '105k', likes: '85k', comments: '15k', shares: '485',
    author: '@blogerich', subs: '384.5K', avatarBg: 'linear-gradient(135deg, #667eea, #764ba2)',
    text: '500 000 лайков на ютубе делаем , бля буду скидываю 😎😎',
    date: '12.12.2025', overlayText: '', overlayEn: '',
  },
  {
    id: 2,
    thumb: thumbs.woman1,
    views: '105k', likes: '85k', comments: '15k', shares: '485',
    author: '@blogerich', subs: '384.5K', avatarBg: 'linear-gradient(135deg, #667eea, #764ba2)',
    text: '500 000 лайков на ютубе делаем , бля буду скидываю 😎😎',
    date: '12.12.2025', overlayText: '', overlayEn: '',
  },
  {
    id: 3,
    thumb: thumbs.woman2,
    views: '105k', likes: '85k', comments: '15k', shares: '485',
    author: '@blogerich', subs: '384.5K', avatarBg: 'linear-gradient(135deg, #ee5a6f, #f09819)',
    text: '500 000 лайков на ютубе делаем , бля буду скидываю 😎😎',
    date: '12.12.2025',
    overlayEn: 'Reading labels you cannot pronounce',
    overlayText: 'тащить матрас по лестнице; читать этикетки, которые не можешь произнести;',
  },
  {
    id: 4,
    thumb: thumbs.woman3,
    views: '105k', likes: '85k', comments: '15k', shares: '485',
    author: '@blogerich', subs: '384.5K', avatarBg: 'linear-gradient(135deg, #ee5a6f, #f09819)',
    text: '500 000 лайков на ютубе делаем , бля буду скидываю 😎😎',
    date: '12.12.2025',
    overlayEn: 'Reading labels you cannot pronounce',
    overlayText: 'тащить матрас по лестнице; читать этикетки, которые не можешь произнести;',
  },
  {
    id: 5,
    thumb: thumbs.man,
    views: '105k', likes: '85k', comments: '15k', shares: '485',
    author: '@blogerich', subs: '384.5K', avatarBg: 'linear-gradient(135deg, #667eea, #764ba2)',
    text: '500 000 лайков на ютубе делаем , бля буду скидываю 😎😎',
    date: '12.12.2025', overlayText: '', overlayEn: '',
  },
  {
    id: 6,
    thumb: thumbs.woman1,
    views: '105k', likes: '85k', comments: '15k', shares: '485',
    author: '@blogerich', subs: '384.5K', avatarBg: 'linear-gradient(135deg, #667eea, #764ba2)',
    text: '500 000 лайков на ютубе делаем , бля буду скидываю 😎😎',
    date: '12.12.2025', overlayText: '', overlayEn: '',
  },
  {
    id: 7,
    thumb: thumbs.woman2,
    views: '105k', likes: '85k', comments: '15k', shares: '485',
    author: '@blogerich', subs: '384.5K', avatarBg: 'linear-gradient(135deg, #ee5a6f, #f09819)',
    text: '500 000 лайков на ютубе делаем , бля буду скидываю 😎😎',
    date: '12.12.2025',
    overlayEn: 'Reading labels you cannot pronounce',
    overlayText: 'тащить матрас по лестнице; читать этикетки, которые не можешь произнести;',
  },
  {
    id: 8,
    thumb: thumbs.woman3,
    views: '105k', likes: '85k', comments: '15k', shares: '485',
    author: '@blogerich', subs: '384.5K', avatarBg: 'linear-gradient(135deg, #ee5a6f, #f09819)',
    text: '500 000 лайков на ютубе делаем , бля буду скидываю 😎😎',
    date: '12.12.2025',
    overlayEn: 'Reading labels you cannot pronounce',
    overlayText: 'тащить матрас по лестнице; читать этикетки, которые не можешь произнести;',
  },
]
</script>

<style scoped>
.page-layout {
  display: flex;
  min-height: 100vh;
  background: #FAFAFA;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* ===== SIDEBAR ===== */
.sidebar {
  width: 244px;
  min-width: 244px;
  background: #fff;
  border-right: 1px solid #F0F0F0;
  display: flex;
  flex-direction: column;
  padding: 20px 0;
  height: 100vh;
  position: sticky;
  top: 0;
  overflow-y: auto;
  overflow-x: hidden;
}

.sidebar-logo {
  padding: 0 20px;
  margin-bottom: 28px;
}

.logo-img {
  height: 24px;
  width: auto;
}

.sidebar-section {
  margin-bottom: 16px;
}

.section-label {
  font-size: 11px;
  font-weight: 500;
  color: #999;
  padding: 0 20px;
  margin-bottom: 4px;
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 20px;
  color: #444;
  text-decoration: none;
  font-size: 14px;
  font-weight: 400;
  transition: all 0.15s;
  position: relative;
}

.nav-item:hover {
  background: #F8F8FA;
  color: #222;
}

.nav-item.active {
  color: #4F46E5;
  background: #F5F3FF;
  font-weight: 500;
}

.nav-item.disabled {
  opacity: 0.45;
  pointer-events: none;
}

.nav-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.nav-badge {
  margin-left: auto;
  background: #4F46E5;
  color: #fff;
  font-size: 11px;
  padding: 1px 8px;
  border-radius: 10px;
  font-weight: 600;
}

.nav-soon {
  margin-left: auto;
  font-size: 11px;
  color: #bbb;
  font-weight: 400;
}

/* Sidebar bottom */
.sidebar-bottom {
  margin-top: auto;
  padding: 0 16px;
}

.token-bar {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 6px;
}

.token-icon {
  font-size: 16px;
}

.token-label {
  font-size: 13px;
  font-weight: 600;
  color: #333;
}

.token-count {
  margin-left: auto;
  font-size: 13px;
  color: #666;
  font-weight: 500;
}

.token-progress {
  height: 4px;
  background: #E8E5FF;
  border-radius: 2px;
  margin-bottom: 16px;
  overflow: hidden;
}

.token-progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #4F46E5, #6C5CE7);
  border-radius: 2px;
}

.creative-plus {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 4px;
  font-size: 14px;
  color: #333;
  cursor: pointer;
  border-radius: 8px;
  margin-bottom: 12px;
}

.creative-plus:hover {
  background: #f8f8fa;
}

.sidebar-user {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 4px;
  border-top: 1px solid #F0F0F0;
}

.user-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
  background: #E8E5FF;
}

.user-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.user-info {
  flex: 1;
  min-width: 0;
}

.user-name {
  font-size: 13px;
  font-weight: 600;
  color: #333;
}

.user-phone {
  font-size: 11px;
  color: #999;
}

.logout-icon {
  cursor: pointer;
  flex-shrink: 0;
  opacity: 0.5;
}

.lang-selector {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 4px;
  font-size: 13px;
  color: #666;
  cursor: pointer;
}

/* ===== MAIN CONTENT ===== */
.main-content {
  flex: 1;
  padding: 16px 24px 32px;
  overflow-y: auto;
}

.video-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

/* ===== VIDEO CARD ===== */
.video-card {
  background: #fff;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}

.card-thumbnail {
  position: relative;
  height: 280px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  background: #1a1a2e;
}

.thumb-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.thumb-top {
  position: absolute;
  top: 10px;
  left: 10px;
  right: 10px;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  z-index: 2;
}

.reels-badge {
  display: flex;
  align-items: center;
  gap: 4px;
  background: rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(8px);
  padding: 4px 10px;
  border-radius: 6px;
  color: #fff;
  font-size: 12px;
  font-weight: 600;
}

.thumb-heart {
  cursor: pointer;
  opacity: 0.9;
}

.thumb-heart:hover {
  opacity: 1;
}

.thumb-badges {
  position: absolute;
  top: 42px;
  left: 10px;
  z-index: 2;
}

.x10-badge {
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(4px);
  color: #fff;
  font-size: 11px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 5px;
}

.thumb-bottom-right {
  position: absolute;
  bottom: 10px;
  right: 10px;
  width: 28px;
  height: 28px;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 2;
}

.thumb-overlay-text {
  position: absolute;
  bottom: 40px;
  left: 10px;
  right: 10px;
  z-index: 2;
}

.overlay-en {
  font-size: 14px;
  font-weight: 600;
  color: #fff;
  text-shadow: 0 1px 4px rgba(0,0,0,0.5);
  margin-bottom: 6px;
}

.overlay-ru {
  font-size: 11px;
  color: #fff;
  background: rgba(0, 0, 0, 0.55);
  padding: 6px 8px;
  border-radius: 6px;
  line-height: 1.3;
}

/* Stats Bar */
.stats-bar {
  display: flex;
  justify-content: space-around;
  padding: 8px 8px;
  background: #2D2D3F;
}

.stat {
  display: flex;
  align-items: center;
  gap: 3px;
  color: #fff;
  font-size: 11px;
  font-weight: 500;
}

/* Card Info */
.card-info {
  padding: 12px 14px 14px;
}

.card-author {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}

.author-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  flex-shrink: 0;
}

.author-details {
  flex: 1;
  min-width: 0;
}

.author-name {
  display: block;
  font-size: 13px;
  font-weight: 600;
  color: #333;
}

.author-subs {
  display: block;
  font-size: 11px;
  color: #999;
}

.author-actions {
  display: flex;
  gap: 4px;
  flex-shrink: 0;
}

.card-text {
  font-size: 12px;
  color: #444;
  line-height: 1.4;
  margin-bottom: 6px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-date {
  font-size: 11px;
  color: #BBB;
  margin-bottom: 10px;
}

.card-btn {
  width: 100%;
  padding: 9px;
  background: #4F46E5;
  color: #fff;
  border: none;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s;
}

.card-btn:hover {
  background: #4338CA;
}

/* Load More */
.load-more-area {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 32px 0 16px;
}

.load-more-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 28px;
  background: #4F46E5;
  color: #fff;
  border: none;
  border-radius: 12px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s;
}

.load-more-btn:hover {
  background: #4338CA;
}

.video-counter {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: #666;
  font-weight: 500;
}

/* Responsive */
@media (max-width: 1400px) {
  .video-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 1100px) {
  .video-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 800px) {
  .sidebar {
    display: none;
  }
  .video-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
