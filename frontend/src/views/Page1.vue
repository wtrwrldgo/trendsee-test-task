<template>
  <div class="page-layout">
    <!-- Sidebar -->
    <aside class="sidebar">
      <div class="sidebar-logo">
        <img src="/logo.png" alt="trendsee" class="logo-img" />
        <span class="logo-beta">Beta</span>
      </div>

      <div class="sidebar-section">
        <div class="section-label">Поиск контента</div>
        <nav class="sidebar-nav">
          <a href="#" class="nav-item active">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><path d="M3 10l7-7 7 7M5 8v8a1 1 0 001 1h3v-4h2v4h3a1 1 0 001-1V8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <span>Главная</span>
          </a>
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><rect x="3" y="3" width="14" height="14" rx="2" stroke="currentColor" stroke-width="1.5"/><polygon points="8,6 8,14 14,10" fill="currentColor"/></svg>
            <span>Видео</span>
          </a>
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="7" stroke="currentColor" stroke-width="1.5"/><circle cx="10" cy="10" r="2.5" fill="currentColor"/></svg>
            <span>Контент-радар</span>
          </a>
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><path d="M10 3a7 7 0 100 14 7 7 0 000-14zm0 3v4l3 2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            <span>Шпионаж</span>
          </a>
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><path d="M10 3l2 4h4l-3 3 1 4-4-2-4 2 1-4-3-3h4z" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>
            <span>Аномальные видео</span>
          </a>
        </nav>
      </div>

      <div class="sidebar-section">
        <div class="section-label">Инструменты</div>
        <nav class="sidebar-nav">
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><path d="M10 4v12M4 10h12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><circle cx="10" cy="10" r="7" stroke="currentColor" stroke-width="1.5"/></svg>
            <span>Анализ видео</span>
          </a>
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="7" r="3.5" stroke="currentColor" stroke-width="1.5"/><path d="M3 18c0-3.9 3.1-7 7-7s7 3.1 7 7" stroke="currentColor" stroke-width="1.5"/></svg>
            <span>Анализ профиля</span>
          </a>
        </nav>
      </div>

      <div class="sidebar-section">
        <div class="section-label">Идеи</div>
        <nav class="sidebar-nav">
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><path d="M10 3C6.5 3 4 5.5 4 8.5c0 2 1 3.5 2.5 4.5.5.3.5.7.5 1v1h6v-1c0-.3 0-.7.5-1C15 12 16 10.5 16 8.5 16 5.5 13.5 3 10 3z" stroke="currentColor" stroke-width="1.5"/><path d="M8 17h4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            <span>Избранные</span>
          </a>
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><rect x="3" y="4" width="14" height="12" rx="2" stroke="currentColor" stroke-width="1.5"/><path d="M7 8h6M7 11h4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            <span>Обучение</span>
          </a>
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="7" stroke="currentColor" stroke-width="1.5"/><path d="M10 6v4l2.5 2.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            <span>История</span>
          </a>
        </nav>
      </div>

      <div class="sidebar-section">
        <div class="section-label">Ещё</div>
        <nav class="sidebar-nav">
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><path d="M10 4v12M4 10h12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            <span>Предложить идею</span>
          </a>
          <a href="#" class="nav-item">
            <svg class="nav-icon" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="7" stroke="currentColor" stroke-width="1.5"/><path d="M10 7v3M10 13h.01" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            <span>Поддержка</span>
          </a>
        </nav>
      </div>

      <div class="sidebar-bottom">
        <div class="promo-banner">
          <div class="promo-text">
            <span class="promo-label">Платим за кейсы</span>
            <span class="promo-sub">Подробнее</span>
          </div>
          <div class="promo-badge">
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><polygon points="7,1 7,13 1,7 13,7" fill="white"/></svg>
            100k
          </div>
          <button class="promo-close">&times;</button>
        </div>

        <div class="token-bar">
          <span class="token-icon">🔥</span>
          <span class="token-label">Осталось токенов:</span>
          <span class="token-count">150</span>
        </div>

        <a href="#" class="tariff-link">Открыть тарифы <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M4 2l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></a>

        <div class="sidebar-user">
          <div class="user-avatar">
            <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Musabek" alt="" />
          </div>
          <div class="user-info">
            <div class="user-name">Musabek Isakov</div>
          </div>
          <svg class="logout-icon" width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M8 3H5a2 2 0 00-2 2v10a2 2 0 002 2h3M13 14l4-4-4-4M17 10H8" stroke="#999" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="main-content">
      <!-- Header -->
      <div class="page-header">
        <h1 class="greeting">Что будем искать сегодня, Musabek Isakov?</h1>
        <div class="search-bar">
          <div class="search-input-wrap">
            <svg class="search-icon" width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="9" cy="9" r="6" stroke="white" stroke-width="1.5"/><path d="M14 14l3 3" stroke="white" stroke-width="1.5" stroke-linecap="round"/></svg>
            <input type="text" class="search-input" placeholder="Введите запрос" />
          </div>
          <button class="search-type-btn">
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="2" y="2" width="12" height="12" rx="3" stroke="currentColor" stroke-width="1.5"/><rect x="5" y="5" width="3" height="6" fill="currentColor"/><rect x="9" y="3" width="3" height="10" fill="currentColor" fill-opacity="0.5"/></svg>
            Reels
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M3 5l3 3 3-3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
          </button>
          <button class="search-submit-btn">
            Поиск
            <span class="search-fire">🔥</span>
            <span class="search-count">1</span>
          </button>
          <div class="search-hint">Введите запрос, а мы найдем для Вас видео &nbsp; Тип видео</div>
        </div>
      </div>

      <!-- Section heading -->
      <div class="section-heading">
        <h2 class="section-title">Банк идей</h2>
        <p class="section-subtitle">Тут можно посмотреть видео по подборкам</p>
      </div>

      <!-- Video Grid -->
      <div class="video-grid">
        <div v-for="card in cards" :key="card.id" class="video-card">
          <div class="card-thumbnail">
            <div class="thumb-top">
              <div class="reels-badge">
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><rect width="14" height="14" rx="3" fill="white" fill-opacity="0.3"/><rect x="2" y="4" width="4" height="6" fill="white"/><rect x="7" y="2" width="5" height="10" fill="white" fill-opacity="0.6"/></svg>
                Reels
              </div>
              <svg class="thumb-heart" width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 21C12 21 3 13.5 3 8.5C3 5.42 5.42 3 8.5 3C10.24 3 11.91 3.81 12 5C12.09 3.81 13.76 3 15.5 3C18.58 3 21 5.42 21 8.5C21 13.5 12 21 12 21Z" stroke="white" stroke-width="1.5"/></svg>
            </div>
            <div v-if="card.x10" class="thumb-badges">
              <span class="x10-badge">🔥 X{{ card.x10 }}</span>
            </div>
            <div class="thumb-bottom-right">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M3 7l4-4m0 0l4 4M7 3v12" stroke="white" stroke-width="1.5" stroke-linecap="round"/></svg>
            </div>
            <img :src="card.thumb" :alt="card.author" class="thumb-img" />
            <div v-if="card.overlayText" class="thumb-overlay-text">
              {{ card.overlayText }}
            </div>
            <div v-if="card.hasPlay" class="thumb-play">
              <svg width="40" height="40" viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" fill="rgba(255,255,255,0.25)"/><polygon points="16,12 16,28 30,20" fill="white"/></svg>
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
              <div class="author-avatar" :style="{ background: card.avatarBg }">
                <img v-if="card.avatarImg" :src="card.avatarImg" alt="" />
              </div>
              <div class="author-details">
                <span class="author-name">{{ card.author }}</span>
                <span class="author-subs">{{ card.subs }}</span>
              </div>
              <div class="author-actions">
                <svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9 3v12M3 9h12" stroke="#999" stroke-width="1.5" stroke-linecap="round"/></svg>
                <svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M3 6h12M3 9h12M3 12h12" stroke="#999" stroke-width="1.2" stroke-linecap="round"/></svg>
              </div>
            </div>
            <p class="card-text">{{ card.text }}</p>
            <div class="card-date">{{ card.date }}</div>
            <button class="card-btn">Анализ видео</button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
const cards = [
  {
    id: 1,
    thumb: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&h=560&fit=crop&crop=face',
    views: '42.6k', likes: '3.3k', comments: '27', shares: '153',
    author: '@goshanegosha_', subs: '-', avatarBg: 'linear-gradient(135deg, #f5af19, #f12711)',
    avatarImg: '',
    text: 'всем по сочному апельсину',
    date: 'сегодня', overlayText: '', x10: 0, hasPlay: true,
  },
  {
    id: 2,
    thumb: 'https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?w=400&h=560&fit=crop&crop=face',
    views: '11.3k', likes: '120', comments: '0', shares: '18',
    author: '@themlyanova.brows', subs: '-', avatarBg: '#333',
    avatarImg: '',
    text: '↓ Как ведут себя клиенты в 2026? Если кратко, то период...',
    date: 'вчера',
    overlayText: 'САМОЕ ГЛАВНОЕ ИЗМЕНЕНИЕ В ПОВЕДЕНИИ КЛИЕНТА',
    x10: 0, hasPlay: false,
  },
  {
    id: 3,
    thumb: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400&h=560&fit=crop&crop=face',
    views: '5.1k', likes: '71', comments: '1', shares: '1',
    author: '@themlyanova.brows', subs: '-', avatarBg: '#333',
    avatarImg: '',
    text: '↓ Как вернуть охваты? Охваты в инсте упали у всех, и у меня тоже. Я ка...',
    date: 'сегодня',
    overlayText: 'ОХВАТЫ В ИНСТЕ УПАЛИ У ВСЕХ',
    x10: 0, hasPlay: false,
  },
  {
    id: 4,
    thumb: 'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=400&h=560&fit=crop&crop=face',
    views: '92k', likes: '652', comments: '36', shares: '715',
    author: '-', subs: '-', avatarBg: '#ccc',
    avatarImg: '',
    text: '🇦🇪 В Дубае зафиксирован удар по территории международного...',
    date: '1 неделя назад', overlayText: '', x10: 14, hasPlay: false,
  },
  {
    id: 5,
    thumb: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=560&fit=crop&crop=face',
    views: '12.7k', likes: '212', comments: '14', shares: '100',
    author: '-', subs: '-', avatarBg: '#ddd',
    avatarImg: '',
    text: 'Я — Ревизор недвижимости Турции. 🇹🇷 7+ лет в Аланье Говор...',
    date: '1 неделя назад',
    overlayText: 'Пора выходить на рынок ОАЭ, там надежно и стабильно',
    x10: 0, hasPlay: false,
  },
  {
    id: 6,
    thumb: 'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=400&h=560&fit=crop&crop=face',
    views: '8.4k', likes: '430', comments: '12', shares: '67',
    author: '@beauty_master', subs: '12.3K', avatarBg: 'linear-gradient(135deg, #667eea, #764ba2)',
    avatarImg: '',
    text: 'Топ-5 ошибок при уходе за кожей зимой ❄️ Сохраняй чтобы не забыть!',
    date: '2 дня назад', overlayText: '', x10: 0, hasPlay: false,
  },
  {
    id: 7,
    thumb: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&h=560&fit=crop&crop=face',
    views: '33.1k', likes: '1.2k', comments: '89', shares: '234',
    author: '@marketolog_pro', subs: '56.7K', avatarBg: 'linear-gradient(135deg, #ee5a6f, #f09819)',
    avatarImg: '',
    text: 'Как запустить рекламу с нуля? Пошаговый гайд для новичков 🚀',
    date: '3 дня назад', overlayText: '', x10: 0, hasPlay: true,
  },
  {
    id: 8,
    thumb: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&h=560&fit=crop&crop=face',
    views: '19.5k', likes: '890', comments: '45', shares: '312',
    author: '@fitness_coach', subs: '28.9K', avatarBg: 'linear-gradient(135deg, #11998e, #38ef7d)',
    avatarImg: '',
    text: 'Утренняя тренировка за 10 минут 💪 Результат уже через неделю!',
    date: 'вчера', overlayText: '', x10: 0, hasPlay: false,
  },
  {
    id: 9,
    thumb: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=400&h=560&fit=crop&crop=face',
    views: '67.2k', likes: '4.5k', comments: '156', shares: '890',
    author: '@travel_blog', subs: '102K', avatarBg: 'linear-gradient(135deg, #4facfe, #00f2fe)',
    avatarImg: '',
    text: 'Бали 2026: что изменилось? Честный обзор для тех кто собирается 🌴',
    date: 'сегодня', overlayText: '', x10: 0, hasPlay: false,
  },
  {
    id: 10,
    thumb: 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=400&h=560&fit=crop&crop=face',
    views: '15.8k', likes: '670', comments: '23', shares: '145',
    author: '@dev_stories', subs: '8.4K', avatarBg: 'linear-gradient(135deg, #a18cd1, #fbc2eb)',
    avatarImg: '',
    text: 'Мой путь в IT: от курьера до разработчика за 8 месяцев 💻',
    date: '5 дней назад', overlayText: '', x10: 0, hasPlay: true,
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
  display: flex;
  align-items: center;
  gap: 8px;
}

.logo-img {
  height: 24px;
  width: auto;
}

.logo-beta {
  font-size: 10px;
  font-weight: 600;
  color: #666;
  background: #f0f0f0;
  padding: 2px 6px;
  border-radius: 4px;
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
  text-transform: none;
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

.nav-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

/* Sidebar bottom */
.sidebar-bottom {
  margin-top: auto;
  padding: 0 16px;
}

.promo-banner {
  background: linear-gradient(135deg, #7c3aed, #ec4899);
  border-radius: 12px;
  padding: 10px 12px;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 16px;
  position: relative;
  color: #fff;
}

.promo-text {
  display: flex;
  flex-direction: column;
}

.promo-label {
  font-size: 12px;
  font-weight: 700;
  color: #fff;
}

.promo-sub {
  font-size: 10px;
  color: rgba(255, 255, 255, 0.8);
}

.promo-badge {
  display: flex;
  align-items: center;
  gap: 4px;
  background: rgba(0, 0, 0, 0.2);
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 700;
  margin-left: auto;
}

.promo-close {
  position: absolute;
  top: 2px;
  right: 6px;
  background: none;
  border: none;
  color: rgba(255, 255, 255, 0.6);
  font-size: 16px;
  cursor: pointer;
  padding: 0;
  line-height: 1;
}

.token-bar {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 8px;
}

.token-icon {
  font-size: 16px;
}

.token-label {
  font-size: 13px;
  font-weight: 500;
  color: #333;
}

.token-count {
  margin-left: auto;
  font-size: 14px;
  color: #333;
  font-weight: 700;
}

.tariff-link {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 13px;
  color: #666;
  text-decoration: none;
  padding: 6px 0;
  margin-bottom: 12px;
}

.tariff-link:hover {
  color: #4F46E5;
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

.logout-icon {
  cursor: pointer;
  flex-shrink: 0;
  opacity: 0.5;
}

/* ===== MAIN CONTENT ===== */
.main-content {
  flex: 1;
  padding: 0 24px 32px;
  overflow-y: auto;
}

/* Header */
.page-header {
  padding: 20px 0 24px;
}

.greeting {
  font-size: 22px;
  font-weight: 600;
  color: #1a1a2e;
  margin-bottom: 16px;
}

.search-bar {
  background: linear-gradient(135deg, #7c3aed, #a78bfa, #818cf8);
  border-radius: 16px;
  padding: 24px 24px 12px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  position: relative;
}

.search-input-wrap {
  flex: 1;
  min-width: 200px;
  position: relative;
  display: flex;
  align-items: center;
}

.search-icon {
  position: absolute;
  left: 14px;
  opacity: 0.7;
}

.search-input {
  width: 100%;
  padding: 12px 16px 12px 44px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
  font-size: 15px;
  outline: none;
  backdrop-filter: blur(4px);
}

.search-input::placeholder {
  color: rgba(255, 255, 255, 0.7);
}

.search-input:focus {
  border-color: rgba(255, 255, 255, 0.5);
  background: rgba(255, 255, 255, 0.2);
}

.search-type-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 12px 16px;
  background: rgba(255, 255, 255, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 12px;
  color: #fff;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  backdrop-filter: blur(4px);
}

.search-submit-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 12px 24px;
  background: #fff;
  border: none;
  border-radius: 12px;
  color: #1a1a2e;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
}

.search-submit-btn:hover {
  background: #f5f5f5;
}

.search-fire {
  font-size: 14px;
}

.search-count {
  background: #ef4444;
  color: #fff;
  font-size: 11px;
  font-weight: 700;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.search-hint {
  width: 100%;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.6);
  padding-top: 4px;
}

/* Section heading */
.section-heading {
  margin-bottom: 20px;
}

.section-title {
  font-size: 22px;
  font-weight: 700;
  color: #1a1a2e;
  margin-bottom: 4px;
}

.section-subtitle {
  font-size: 14px;
  color: #888;
}

/* ===== VIDEO GRID — 5 columns ===== */
.video-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
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
  aspect-ratio: 9 / 14;
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
  font-size: 13px;
  font-weight: 700;
  color: #fff;
  text-shadow: 0 1px 6px rgba(0,0,0,0.7);
  line-height: 1.3;
  text-transform: uppercase;
}

.thumb-play {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
  opacity: 0.9;
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
  overflow: hidden;
}

.author-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
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
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
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

/* Responsive */
@media (max-width: 1600px) {
  .video-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (max-width: 1200px) {
  .video-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 900px) {
  .video-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 800px) {
  .sidebar {
    display: none;
  }
}
</style>
