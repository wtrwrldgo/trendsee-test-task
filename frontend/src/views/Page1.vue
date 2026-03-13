<template>
  <div class="page-layout">
    <!-- Sidebar -->
    <aside class="sidebar">
      <div class="sidebar-logo">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
          <circle cx="12" cy="12" r="10" stroke="#6C5CE7" stroke-width="2" />
          <circle cx="12" cy="12" r="4" fill="#6C5CE7" />
        </svg>
        <span class="logo-text">trendsee</span>
        <span class="logo-badge">Beta</span>
      </div>

      <div class="sidebar-section">
        <div class="section-label">Поиск контента</div>
        <nav class="sidebar-nav">
          <a href="#" class="nav-item active">
            <span class="nav-icon">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <path d="M2 2h6v6H2V2zm8 0h6v6h-6V2zm-8 8h6v6H2v-6zm8 0h6v6h-6v-6z" stroke="currentColor" stroke-width="1.5" />
              </svg>
            </span>
            <span>Главная</span>
          </a>
          <a href="#" class="nav-item">
            <span class="nav-icon">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <polygon points="7,2 7,16 15,9" stroke="currentColor" stroke-width="1.5" fill="none" />
              </svg>
            </span>
            <span>Видео</span>
          </a>
          <a href="#" class="nav-item">
            <span class="nav-icon">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <circle cx="9" cy="9" r="7" stroke="currentColor" stroke-width="1.5" />
                <circle cx="9" cy="9" r="2" fill="currentColor" />
              </svg>
            </span>
            <span>Шпионаж</span>
          </a>
          <a href="#" class="nav-item">
            <span class="nav-icon">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <circle cx="9" cy="9" r="7" stroke="currentColor" stroke-width="1.5" />
                <path d="M9 4v5l3 3" stroke="currentColor" stroke-width="1.5" />
              </svg>
            </span>
            <span>Контент радар</span>
            <span class="nav-badge">712</span>
          </a>
        </nav>
      </div>

      <div class="sidebar-section">
        <div class="section-label">Работа с соцсетями</div>
        <nav class="sidebar-nav">
          <a href="#" class="nav-item">
            <span class="nav-icon">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <path d="M4 9h10M9 4v10" stroke="currentColor" stroke-width="1.5" />
              </svg>
            </span>
            <span>Кросс-постинг</span>
          </a>
          <a href="#" class="nav-item">
            <span class="nav-icon">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <rect x="2" y="4" width="14" height="10" rx="2" stroke="currentColor" stroke-width="1.5" />
                <path d="M6 8h6M6 11h4" stroke="currentColor" stroke-width="1.5" />
              </svg>
            </span>
            <span>Чат боты</span>
          </a>
        </nav>
      </div>

      <div class="sidebar-section">
        <div class="section-label">Инструменты</div>
        <nav class="sidebar-nav">
          <a href="#" class="nav-item">
            <span class="nav-icon">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <path d="M3 14l4-8 3 4 2-3 3 7H3z" stroke="currentColor" stroke-width="1.5" fill="none" />
              </svg>
            </span>
            <span>АИ-сценарий</span>
          </a>
          <a href="#" class="nav-item">
            <span class="nav-icon">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <rect x="2" y="2" width="14" height="14" rx="2" stroke="currentColor" stroke-width="1.5" />
                <rect x="5" y="5" width="8" height="8" rx="1" stroke="currentColor" stroke-width="1" />
              </svg>
            </span>
            <span>Карусели</span>
          </a>
          <a href="#" class="nav-item">
            <span class="nav-icon">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <polygon points="7,2 7,16 15,9" stroke="currentColor" stroke-width="1.5" fill="none" />
              </svg>
            </span>
            <span>Анализ видео</span>
          </a>
          <a href="#" class="nav-item">
            <span class="nav-icon">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <circle cx="9" cy="6" r="3" stroke="currentColor" stroke-width="1.5" />
                <path d="M3 16c0-3.3 2.7-6 6-6s6 2.7 6 6" stroke="currentColor" stroke-width="1.5" />
              </svg>
            </span>
            <span>Анализ профиля</span>
          </a>
          <a href="#" class="nav-item disabled">
            <span class="nav-icon">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <rect x="3" y="3" width="12" height="12" rx="2" stroke="currentColor" stroke-width="1.5" />
              </svg>
            </span>
            <span>Черновик</span>
            <span class="nav-soon">Скоро</span>
          </a>
        </nav>
      </div>

      <div class="sidebar-bottom">
        <div class="token-bar">
          <div class="token-icon">
            <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
              <circle cx="9" cy="9" r="7" stroke="#6C5CE7" stroke-width="1.5" />
              <path d="M9 5v8M7 7l2-2 2 2M7 11l2 2 2-2" stroke="#6C5CE7" stroke-width="1.2" />
            </svg>
          </div>
          <span class="token-label">Токены</span>
          <span class="token-count">1 245 / 4 497</span>
        </div>

        <div class="creative-plus">
          <span>Creative +</span>
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M6 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" />
          </svg>
        </div>

        <div class="sidebar-user">
          <div class="user-avatar">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
              <circle cx="16" cy="16" r="15" fill="#E8E5FF" />
              <circle cx="16" cy="13" r="5" fill="#6C5CE7" />
              <path d="M6 28c0-5.5 4.5-10 10-10s10 4.5 10 10" fill="#6C5CE7" />
            </svg>
          </div>
          <div class="user-info">
            <div class="user-name">Александра</div>
            <div class="user-phone">+7 (999) 999-99-99</div>
          </div>
          <svg class="logout-icon" width="18" height="18" viewBox="0 0 18 18" fill="none">
            <path d="M7 2H4a2 2 0 00-2 2v10a2 2 0 002 2h3M11 13l4-4-4-4M15 9H7" stroke="#999" stroke-width="1.5" />
          </svg>
        </div>

        <div class="lang-selector">
          <span class="lang-flag">🇷🇺</span>
          <span>RU</span>
          <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
            <path d="M3 5l3 3 3-3" stroke="currentColor" stroke-width="1.5" />
          </svg>
        </div>
      </div>
    </aside>

    <!-- Main Content - Video Cards + Analysis -->
    <div class="main-area">
      <!-- Video Column -->
      <div class="video-column">
        <div class="video-card">
          <div class="video-preview">
            <div class="video-image" style="background: linear-gradient(180deg, #2a1a3e 0%, #1a0a2e 100%);">
              <div class="video-overlay-top">
                <div class="reels-badge">
                  <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
                    <rect width="12" height="12" rx="3" fill="white" fill-opacity="0.2" />
                  </svg>
                  Reels
                </div>
                <div class="video-right-icons">
                  <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                    <path d="M10 4l1.5 3 3.5.5-2.5 2.5.5 3.5L10 12l-3 1.5.5-3.5L5 7.5 8.5 7z" fill="white" />
                  </svg>
                </div>
              </div>
              <div class="x10-badge">X10</div>
              <div class="video-placeholder-face"></div>
              <div class="video-play-btn">
                <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
                  <polygon points="12,8 12,24 24,16" fill="white" />
                </svg>
              </div>
            </div>
            <div class="video-stats-row">
              <div class="stat-item">
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                  <path d="M7 2l1.5 3 3.5.5-2.5 2.5.5 3.5L7 10l-3 1.5.5-3.5L2 5.5 5.5 5z" fill="#FF6B6B" />
                </svg>
                <span>105k</span>
              </div>
              <div class="stat-item">
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                  <path d="M2 5h10v7H2z" stroke="#4ECDC4" stroke-width="1.2" fill="none" />
                </svg>
                <span>85k</span>
              </div>
              <div class="stat-item">
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                  <path d="M4 12V6h2v6H4zm4 0V2h2v10H8z" fill="#FFE66D" />
                </svg>
                <span>15k</span>
              </div>
              <div class="stat-item">
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                  <path d="M3 7l3 3 5-5" stroke="#A8E6CF" stroke-width="1.5" />
                </svg>
                <span>485</span>
              </div>
            </div>
          </div>
          <div class="video-card-info">
            <div class="video-author">
              <div class="author-avatar-small"></div>
              <div>
                <div class="author-handle">@blogerich <span class="verified">✦</span></div>
                <div class="author-followers">384.5K</div>
              </div>
            </div>
            <p class="video-description">500 000 лайков на ютубе делаем , бля буду скидываю 😎😎</p>
            <div class="video-date">12.12.2025</div>
            <button class="analyze-btn">Анализ</button>
          </div>
        </div>
      </div>

      <!-- Analysis Column -->
      <div class="analysis-column">
        <!-- Video Preview in Analysis -->
        <div class="analysis-video-section">
          <div class="analysis-video-card">
            <div class="analysis-video-preview" style="background: linear-gradient(180deg, #2a1a3e 0%, #1a0a2e 100%);">
              <div class="reels-badge">
                <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
                  <rect width="12" height="12" rx="3" fill="white" fill-opacity="0.2" />
                </svg>
                Reels
              </div>
              <div class="x10-badge">X10</div>
              <div class="video-placeholder-face"></div>
              <div class="video-play-btn">
                <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
                  <polygon points="12,8 12,24 24,16" fill="white" />
                </svg>
              </div>
              <div class="analysis-video-date">12.12.2025</div>
              <div class="share-icon">
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                  <path d="M4 8l4-4 4 4M8 4v8" stroke="white" stroke-width="1.5" />
                </svg>
              </div>
            </div>
            <div class="analysis-video-info">
              <div class="video-author">
                <div class="author-avatar-small"></div>
                <div>
                  <div class="author-handle">@blogerich <span class="verified">✦</span></div>
                  <div class="author-followers">384.5K</div>
                </div>
              </div>
              <p class="video-description-sm">Чтобы выиграть в этой игре, нужно быть настоящим психопа...</p>
              <div class="more-link">Ещё</div>

              <div class="analysis-stats">
                <div class="stat-row">
                  <span class="stat-icon views">👁</span>
                  <span class="stat-name">Просмотры</span>
                  <span class="stat-value">1,2 млн</span>
                </div>
                <div class="stat-row">
                  <span class="stat-icon likes">❤</span>
                  <span class="stat-name">Лайки</span>
                  <span class="stat-value">1,2 млн</span>
                </div>
                <div class="stat-row">
                  <span class="stat-icon comments">💬</span>
                  <span class="stat-name">Комментарии</span>
                  <span class="stat-value">1,2 млн</span>
                </div>
                <div class="stat-row">
                  <span class="stat-icon reposts">↗</span>
                  <span class="stat-name">Репосты</span>
                  <span class="stat-value">1,2 млн</span>
                </div>
                <div class="stat-row">
                  <span class="stat-icon er">📊</span>
                  <span class="stat-name">ER</span>
                  <span class="stat-value">1,2 млн</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Analysis Detail Panel -->
        <div class="analysis-detail">
          <button class="close-btn">&times;</button>

          <div class="detail-section">
            <div class="detail-label">Тема видео</div>
            <h2 class="detail-title">Рассуждения на тему правильности и неправильности</h2>
          </div>

          <div class="detail-meta">
            <div class="meta-music">
              <span class="music-icon">🎵</span>
              <span>Tyga – Pop it off</span>
            </div>
            <div class="meta-lang">
              <span>Язык:</span>
              <span class="lang-flag-sm">🇬🇧</span>
              <span>Английский</span>
            </div>
          </div>

          <div class="tags-row">
            <span class="tag tag-purple">Туториал</span>
            <span class="tag tag-orange">Энергичное видео</span>
            <span class="tag tag-green">Изи монтаж</span>
            <span class="tag tag-red">Трендовый звук</span>
            <span class="tag tag-purple">Лид магнит</span>
            <span class="tag tag-default">Красота и здоровье</span>
          </div>

          <div class="transcription-section">
            <div class="section-header">
              <h3>Транскрибация</h3>
              <div class="section-actions">
                <button class="action-btn translated">
                  <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                    <path d="M2 5h10M5 2v10M8 8l3 3" stroke="currentColor" stroke-width="1.2" />
                  </svg>
                  Переведено
                </button>
                <button class="copy-btn">
                  <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                    <rect x="4" y="4" width="8" height="8" rx="1" stroke="currentColor" stroke-width="1.2" />
                    <path d="M2 10V3a1 1 0 011-1h7" stroke="currentColor" stroke-width="1.2" />
                  </svg>
                </button>
              </div>
            </div>
            <div class="transcription-text">
              <p>SPF скатывается? Смотри — вот эти катышки. И нет, это не всегда "плохой SPF". Скатывается по трём причинам.</p>
              <p>Первая — ты намазал под SPF слишком много всего: сыворотка, крем, база... сверху SPF — и оно начинает конфликтовать. Чем больше слоёв, тем выше шанс, что всё свернётся в катышки....</p>
            </div>
            <div class="more-link">∨ Ещё</div>
          </div>

          <button class="adapt-btn">Адаптировать</button>

          <div class="essence-section">
            <h3>Суть</h3>
            <div class="essence-text">
              <p>Разбор состава/логики: он в человеческих словах переводит состав/механику ("что реально делает Х"), называет 2–3 работающих активных компонента и 2–3 маркетинговых "пустых" обещания.</p>
            </div>
          </div>

          <div class="structure-section">
            <h3>Структура</h3>
            <div class="timeline">
              <div class="timeline-item">
                <span class="time-label">0–3 сек</span>
                <div class="timeline-dot dot-light"></div>
                <div class="timeline-content">
                  <div class="timeline-title">Шок-сравнение</div>
                  <div class="timeline-desc">Визуальный (Девушка с предметом) + Текст на экране: "Это спасет вашу зиму"</div>
                </div>
              </div>
              <div class="timeline-item">
                <span class="time-label">3–15 сек</span>
                <div class="timeline-dot dot-mid"></div>
                <div class="timeline-content">
                  <div class="timeline-title">Сюжет</div>
                  <div class="timeline-desc">[Герой] показывает проблему → Резкар смена кадра → Решение</div>
                </div>
              </div>
              <div class="timeline-item">
                <span class="time-label">15–120 сек</span>
                <div class="timeline-dot dot-dark"></div>
                <div class="timeline-content">
                  <div class="timeline-title">Финал / CTA</div>
                  <div class="timeline-desc">Призыв: "Пиши слово "ССЫЛКА" в комменты"</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.page-layout {
  display: flex;
  min-height: 100vh;
  background: #f5f5f7;
  font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', sans-serif;
}

/* ===== SIDEBAR ===== */
.sidebar {
  width: 240px;
  min-width: 240px;
  background: #fff;
  border-right: 1px solid #eee;
  display: flex;
  flex-direction: column;
  padding: 20px 0;
  height: 100vh;
  position: sticky;
  top: 0;
  overflow-y: auto;
}

.sidebar-logo {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 0 20px;
  margin-bottom: 28px;
}

.logo-text {
  font-size: 18px;
  font-weight: 700;
  color: #1a1a2e;
}

.logo-badge {
  font-size: 10px;
  color: #6C5CE7;
  background: #F0EDFF;
  padding: 2px 6px;
  border-radius: 4px;
  font-weight: 600;
}

.sidebar-section {
  margin-bottom: 20px;
}

.section-label {
  font-size: 11px;
  font-weight: 600;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding: 0 20px;
  margin-bottom: 6px;
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 20px;
  color: #555;
  text-decoration: none;
  font-size: 14px;
  transition: all 0.15s;
  position: relative;
}

.nav-item:hover {
  background: #f8f8fa;
  color: #1a1a2e;
}

.nav-item.active {
  color: #6C5CE7;
  background: #F6F4FF;
  font-weight: 500;
}

.nav-item.active::before {
  content: '';
  position: absolute;
  left: 0;
  top: 4px;
  bottom: 4px;
  width: 3px;
  background: #6C5CE7;
  border-radius: 0 3px 3px 0;
}

.nav-item.disabled {
  opacity: 0.5;
  pointer-events: none;
}

.nav-icon {
  width: 18px;
  height: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.nav-badge {
  margin-left: auto;
  background: #6C5CE7;
  color: #fff;
  font-size: 11px;
  padding: 2px 8px;
  border-radius: 10px;
  font-weight: 600;
}

.nav-soon {
  margin-left: auto;
  font-size: 11px;
  color: #bbb;
}

/* Sidebar bottom */
.sidebar-bottom {
  margin-top: auto;
  padding: 0 16px;
}

.token-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 12px;
  background: #F6F4FF;
  border-radius: 10px;
  margin-bottom: 12px;
}

.token-label {
  font-size: 13px;
  font-weight: 600;
  color: #6C5CE7;
}

.token-count {
  margin-left: auto;
  font-size: 12px;
  color: #888;
}

.creative-plus {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 12px;
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
  padding: 10px 4px;
  border-top: 1px solid #eee;
  margin-top: 8px;
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
}

.lang-selector {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 4px;
  font-size: 13px;
  color: #666;
  cursor: pointer;
}

/* ===== MAIN AREA ===== */
.main-area {
  flex: 1;
  display: flex;
  gap: 0;
  overflow-x: auto;
}

/* Video Column */
.video-column {
  width: 280px;
  min-width: 280px;
  padding: 24px 16px;
}

.video-card {
  width: 248px;
  border-radius: 16px;
  overflow: hidden;
  background: #1a1a2e;
}

.video-preview {
  position: relative;
}

.video-image {
  width: 100%;
  height: 340px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.video-overlay-top {
  position: absolute;
  top: 12px;
  left: 12px;
  right: 12px;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.reels-badge {
  display: flex;
  align-items: center;
  gap: 4px;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(8px);
  padding: 4px 10px;
  border-radius: 6px;
  color: #fff;
  font-size: 12px;
  font-weight: 600;
}

.x10-badge {
  position: absolute;
  top: 44px;
  left: 12px;
  background: #2d2d5e;
  color: #fff;
  font-size: 11px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 5px;
}

.video-placeholder-face {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background: linear-gradient(135deg, #d4a8c8 0%, #c48fb1 50%, #b87699 100%);
  opacity: 0.7;
}

.video-play-btn {
  position: absolute;
  bottom: 50%;
  left: 50%;
  transform: translate(-50%, 50%);
  width: 48px;
  height: 48px;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.video-stats-row {
  display: flex;
  justify-content: space-around;
  padding: 10px 12px;
  background: rgba(0, 0, 0, 0.3);
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 4px;
  color: #fff;
  font-size: 12px;
}

.video-card-info {
  padding: 14px;
  background: #fff;
  border-radius: 0 0 16px 16px;
}

.video-author {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}

.author-avatar-small {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea, #764ba2);
}

.author-handle {
  font-size: 13px;
  font-weight: 600;
  color: #333;
}

.verified {
  color: #6C5CE7;
  font-size: 11px;
}

.author-followers {
  font-size: 11px;
  color: #999;
}

.video-description {
  font-size: 13px;
  color: #444;
  line-height: 1.4;
  margin-bottom: 8px;
}

.video-date {
  font-size: 11px;
  color: #bbb;
  margin-bottom: 12px;
}

.analyze-btn {
  width: 100%;
  padding: 10px;
  background: #6C5CE7;
  color: #fff;
  border: none;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s;
}

.analyze-btn:hover {
  background: #5a4bd1;
}

/* ===== ANALYSIS COLUMN ===== */
.analysis-column {
  flex: 1;
  display: flex;
  gap: 0;
  min-width: 0;
}

.analysis-video-section {
  width: 300px;
  min-width: 300px;
  padding: 24px 12px;
}

.analysis-video-card {
  background: #fff;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
}

.analysis-video-preview {
  height: 300px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.analysis-video-preview .reels-badge {
  position: absolute;
  top: 12px;
  left: 12px;
}

.analysis-video-preview .x10-badge {
  top: 44px;
  left: 12px;
}

.analysis-video-date {
  position: absolute;
  bottom: 12px;
  left: 12px;
  color: rgba(255, 255, 255, 0.7);
  font-size: 11px;
}

.share-icon {
  position: absolute;
  bottom: 12px;
  right: 12px;
  width: 28px;
  height: 28px;
  background: rgba(255, 255, 255, 0.15);
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.analysis-video-info {
  padding: 16px;
}

.video-description-sm {
  font-size: 13px;
  color: #444;
  line-height: 1.4;
  margin-bottom: 4px;
}

.more-link {
  font-size: 13px;
  color: #6C5CE7;
  cursor: pointer;
  margin-bottom: 16px;
}

.analysis-stats {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.stat-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.stat-icon {
  width: 24px;
  text-align: center;
  font-size: 14px;
}

.stat-name {
  font-size: 13px;
  color: #666;
  flex: 1;
}

.stat-value {
  font-size: 13px;
  font-weight: 600;
  color: #333;
}

/* ===== ANALYSIS DETAIL ===== */
.analysis-detail {
  flex: 1;
  padding: 24px;
  background: #fff;
  margin: 24px 24px 24px 0;
  border-radius: 16px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
  position: relative;
  overflow-y: auto;
  max-height: calc(100vh - 48px);
}

.close-btn {
  position: absolute;
  top: 16px;
  right: 16px;
  background: none;
  border: none;
  font-size: 24px;
  color: #ccc;
  cursor: pointer;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
}

.close-btn:hover {
  background: #f5f5f5;
  color: #666;
}

.detail-section {
  margin-bottom: 16px;
}

.detail-label {
  font-size: 12px;
  color: #999;
  margin-bottom: 6px;
}

.detail-title {
  font-size: 22px;
  font-weight: 700;
  color: #1a1a2e;
  line-height: 1.3;
}

.detail-meta {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.meta-music {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: #555;
}

.music-icon {
  font-size: 14px;
}

.meta-lang {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: #555;
}

.lang-flag-sm {
  font-size: 14px;
}

/* Tags */
.tags-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 24px;
}

.tag {
  padding: 5px 14px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 500;
  border: 1.5px solid;
}

.tag-purple {
  color: #6C5CE7;
  border-color: #6C5CE7;
  background: #F6F4FF;
}

.tag-orange {
  color: #E67E22;
  border-color: #E67E22;
  background: #FFF8F0;
}

.tag-green {
  color: #27AE60;
  border-color: #27AE60;
  background: #F0FFF5;
}

.tag-red {
  color: #E74C3C;
  border-color: #E74C3C;
  background: #FFF0EF;
}

.tag-default {
  color: #555;
  border-color: #ddd;
  background: #fafafa;
}

/* Transcription */
.transcription-section {
  margin-bottom: 24px;
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.section-header h3 {
  font-size: 16px;
  font-weight: 700;
  color: #1a1a2e;
}

.section-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 5px 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
  background: #fff;
  font-size: 12px;
  color: #666;
  cursor: pointer;
}

.action-btn.translated {
  color: #6C5CE7;
  border-color: #6C5CE7;
  background: #F6F4FF;
}

.copy-btn {
  padding: 5px 8px;
  border: 1px solid #ddd;
  border-radius: 6px;
  background: #fff;
  cursor: pointer;
  color: #999;
  display: flex;
  align-items: center;
}

.copy-btn:hover {
  border-color: #bbb;
  color: #666;
}

.transcription-text {
  background: #f8f8fa;
  padding: 16px;
  border-radius: 10px;
  font-size: 14px;
  line-height: 1.6;
  color: #444;
}

.transcription-text p {
  margin-bottom: 12px;
}

.transcription-text p:last-child {
  margin-bottom: 0;
}

/* Adapt Button */
.adapt-btn {
  display: inline-flex;
  align-items: center;
  padding: 12px 32px;
  background: #E74C3C;
  color: #fff;
  border: none;
  border-radius: 12px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  margin-bottom: 28px;
  transition: background 0.15s;
}

.adapt-btn:hover {
  background: #d44332;
}

/* Essence */
.essence-section {
  margin-bottom: 28px;
}

.essence-section h3 {
  font-size: 16px;
  font-weight: 700;
  color: #1a1a2e;
  margin-bottom: 12px;
}

.essence-text {
  background: #f8f8fa;
  padding: 16px;
  border-radius: 10px;
  font-size: 14px;
  line-height: 1.6;
  color: #444;
}

/* Structure / Timeline */
.structure-section h3 {
  font-size: 16px;
  font-weight: 700;
  color: #1a1a2e;
  margin-bottom: 16px;
}

.timeline {
  position: relative;
  padding-left: 0;
}

.timeline-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  margin-bottom: 20px;
  position: relative;
}

.time-label {
  width: 72px;
  min-width: 72px;
  font-size: 12px;
  color: #999;
  padding-top: 2px;
  text-align: right;
}

.timeline-dot {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  flex-shrink: 0;
  margin-top: 3px;
  position: relative;
}

.timeline-dot::after {
  content: '';
  position: absolute;
  top: 14px;
  left: 50%;
  transform: translateX(-50%);
  width: 2px;
  height: 40px;
  background: #e0e0e0;
}

.timeline-item:last-child .timeline-dot::after {
  display: none;
}

.dot-light {
  background: #B8C4FF;
  border: 2px solid #D4DBFF;
}

.dot-mid {
  background: #7B8CDE;
  border: 2px solid #A0ADEB;
}

.dot-dark {
  background: #3B4FC4;
  border: 2px solid #5B6FD4;
}

.timeline-content {
  flex: 1;
  min-width: 0;
}

.timeline-title {
  font-size: 14px;
  font-weight: 600;
  color: #1a1a2e;
  margin-bottom: 4px;
}

.timeline-desc {
  font-size: 13px;
  color: #666;
  line-height: 1.4;
}
</style>
