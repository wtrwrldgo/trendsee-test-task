# Frontend Rules

## Stack
- Vue 3 with Composition API (`<script setup lang="ts">`)
- Vite for bundling
- Vue Router for navigation
- Axios for API calls

## Conventions
- Scoped styles in every `.vue` component
- TypeScript interfaces for all API response types
- Composables in `src/composables/` for reusable logic
- API client in `src/api/index.ts` with JWT interceptor

## Design System (from Figma)
- Primary color: `#4F46E5` (indigo)
- Card border-radius: `16px`
- Button border-radius: `10px`
- Font: Inter / system fonts
- Background: `#FAFAFA`
- Card shadow: `0 1px 3px rgba(0, 0, 0, 0.04)`

## Pages
- `/` — Feed view with infinite scroll
- `/video-cart` — Figma Page 1: sidebar + 4-column video grid
- `/analysis` — Figma Page 2: detailed video analysis
