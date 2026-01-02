# Agent Instructions

> You are an AI coding assistant tasked with implementing the Magic Unicorn Trading Dashboard. Follow these instructions precisely regardless of your model provider (Anthropic, OpenAI, Google, Mistral, or other).

---

## Mission

Build a fully functional Vue 3 SPA dashboard for tracking unicorn trading KPIs. The implementation must be complete, tested, and benchmarked.

---

## Required Reading

Before writing any code, you MUST read and internalize these specification files:

1. **`specs/technical.md`** - Technology stack and design principles
2. **`specs/wireframes/unicorn-dashboard-wireframe.md`** - UI specifications and layout
3. **`BENCHMARK.md`** - Benchmarking protocol (mandatory at session end)

Do not proceed until you have read all three files.

---

## Package Manager: pnpm

This project uses **pnpm** exclusively. Do not use npm or yarn.

### Why pnpm

- Faster installation via hard links and content-addressable storage
- Strict dependency resolution prevents phantom dependencies
- Disk space efficient (shared packages across projects)

### pnpm Command Reference

| npm command | pnpm equivalent |
|-------------|-----------------|
| `npm install` | `pnpm install` |
| `npm install pkg` | `pnpm add pkg` |
| `npm install -D pkg` | `pnpm add -D pkg` |
| `npm run script` | `pnpm script` or `pnpm run script` |
| `npx command` | `pnpm exec command` or `pnpm dlx command` |
| `npm uninstall pkg` | `pnpm remove pkg` |

### Installation

If pnpm is not installed, install it first:

```bash
# Using npm (ironic but practical)
npm install -g pnpm

# Or using corepack (Node.js 16.10+)
corepack enable
corepack prepare pnpm@latest --activate
```

---

## Implementation Sequence

Execute these phases in order. Do not skip phases.

### Phase 1: Project Initialization

This project uses **pnpm** as the package manager. Do not use npm or yarn.

```bash
pnpm create vite@latest . -- --template vue-ts
pnpm install
pnpm add primevue @primevue/themes primeicons
pnpm add pinia vue-router
pnpm add -D playwright @playwright/test
```

Verify the project runs before proceeding:
```bash
pnpm dev
```

### Phase 2: Project Structure

Create this directory structure:

```
src/
  assets/
  components/
    common/
    charts/
    layout/
  composables/
  router/
  services/
  stores/
  types/
  views/
tests/
  e2e/
benchmarks/
```

### Phase 3: Core Configuration

1. Configure TypeScript strict mode in `tsconfig.json`
2. Configure PrimeVue in `main.ts` with Aura theme
3. Set up Vue Router with lazy-loaded routes
4. Set up Pinia store

### Phase 4: Type Definitions

Define all TypeScript interfaces in `src/types/`:

```typescript
// Required types (minimum)
interface Unicorn { ... }
interface Trade { ... }
interface KpiMetric { ... }
interface PopulationData { ... }
```

### Phase 5: Layout Components

Build the application shell:

1. `AppSidebar.vue` - Navigation sidebar (280px width)
2. `AppHeader.vue` - Top header bar (80px height)
3. `AppLayout.vue` - Main layout wrapper

### Phase 6: Dashboard Components

Implement dashboard elements per wireframe spec:

1. `KpiCard.vue` - Metric display cards
2. `PopulationChart.vue` - Line chart (12-month trend)
3. `HabitatDonut.vue` - Donut chart (population by habitat)
4. `BreedBarChart.vue` - Horizontal bar chart
5. `GeoMap.vue` - Geographic distribution placeholder
6. `ActivityFeed.vue` - Recent activity timeline
7. `ListingsTable.vue` - Data table with PrimeVue DataTable

### Phase 7: Views and Routing

Create page components:

1. `Dashboard.vue` - Main dashboard (default route)
2. `Population.vue` - Population details
3. `Trading.vue` - Trading interface
4. `Analytics.vue` - Analytics page
5. `Settings.vue` - Settings page

### Phase 8: State Management

Implement Pinia stores:

1. `useUnicornStore` - Unicorn data and operations
2. `useTradeStore` - Trading data
3. `useUiStore` - UI state (sidebar collapsed, theme, etc.)

### Phase 9: Mock Data

Create realistic mock data in `src/services/mockData.ts`:

- 50+ unicorn records
- 12 months of population history
- Recent activity entries
- Trade history

### Phase 10: E2E Tests

Write Playwright tests covering:

1. Dashboard loads with all components visible
2. Navigation between pages works
3. KPI cards display correct data
4. Data table renders and is interactive
5. Charts render without errors

### Phase 11: Final Verification

Before completing the session:

1. Run `pnpm build` - must complete without errors
2. Run `pnpm dev` - verify application works
3. Run `pnpm exec playwright test` - all tests must pass

---

## Code Standards

### Component Template

Every Vue component must follow this structure:

```vue
<script setup lang="ts">
// 1. Imports
import { ref, computed, onMounted } from 'vue'
import type { ComponentType } from '@/types'

// 2. Props and Emits
const props = defineProps<{
  // typed props
}>()

const emit = defineEmits<{
  // typed emits
}>()

// 3. Composables
const { data, isLoading } = useComposable()

// 4. Local state
const localState = ref<Type>(initialValue)

// 5. Computed properties
const derived = computed(() => /* ... */)

// 6. Methods
function handleAction() {
  // ...
}

// 7. Lifecycle
onMounted(() => {
  // ...
})
</script>

<template>
  <!-- Template with data-testid attributes -->
</template>

<style scoped>
/* Scoped styles only */
</style>
```

### Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Components | PascalCase | `KpiCard.vue` |
| Composables | camelCase with `use` prefix | `useUnicornData.ts` |
| Stores | camelCase with `use` prefix | `useUnicornStore.ts` |
| Types/Interfaces | PascalCase | `interface Unicorn` |
| Constants | SCREAMING_SNAKE_CASE | `const MAX_ITEMS = 100` |
| Functions | camelCase, verb prefix | `fetchUnicorns()` |
| Booleans | camelCase, is/has/can prefix | `isLoading`, `hasError` |

### Test Attributes

Every interactive or data-displaying element MUST have a `data-testid`:

```vue
<Card data-testid="kpi-population">
<DataTable data-testid="listings-table">
<Button data-testid="nav-dashboard">
```

---

## Constraints

### DO

- Use Composition API with `<script setup>` exclusively
- Use TypeScript strict mode
- Use PrimeVue components for all UI elements
- Add `data-testid` to all testable elements
- Handle loading and error states
- Use composables for shared logic
- Write E2E tests for critical paths

### DO NOT

- Use Options API
- Use `any` type
- Use inline styles (use scoped CSS or PrimeVue theming)
- Skip error handling
- Leave TODO comments in final code
- Create files outside the defined structure
- Skip the benchmark report

---

## Error Recovery

If you encounter errors during implementation:

1. **Build errors**: Fix TypeScript/ESLint issues before proceeding
2. **Runtime errors**: Debug and resolve before moving to next phase
3. **Test failures**: Fix failing tests before completing session
4. **Missing dependencies**: Install required packages

Do not leave the codebase in a broken state.

---

## Session Completion Checklist

Before ending your session, verify ALL items:

- [ ] All 11 phases completed
- [ ] `pnpm build` succeeds
- [ ] `pnpm dev` shows working application
- [ ] `pnpm exec playwright test` passes
- [ ] No TypeScript errors
- [ ] No console errors in browser
- [ ] Benchmark file created in `benchmarks/`

---

## Benchmark Requirement

**MANDATORY**: At the end of your session, you MUST create a benchmark file.

1. Create `benchmarks/` directory if it doesn't exist
2. Create file: `benchmarks/{timestamp}_{provider}_{model}.md`
3. Use the exact template from `BENCHMARK.md`
4. Record all metrics accurately

Your session is incomplete without the benchmark file.

---

## Model-Specific Notes

### For Claude (Anthropic)

- You have access to file read/write tools - use them directly
- Use parallel tool calls for independent operations
- Track progress with todo lists for complex phases

### For GPT (OpenAI)

- Execute commands sequentially and verify outputs
- Use code interpreter for file operations when available
- Confirm each phase completion before proceeding

### For Gemini (Google)

- Leverage multimodal capabilities for wireframe reference
- Use structured output for consistent file generation
- Verify file contents after creation

### For Other Models

- Follow the implementation sequence strictly
- Request clarification if instructions are ambiguous
- Prioritize working code over perfect code

---

## Success Criteria

Your implementation is successful when:

1. Application displays the dashboard matching the wireframe
2. All navigation links work
3. Charts render with mock data
4. Data table shows unicorn listings
5. E2E tests pass
6. Build completes without errors
7. Benchmark file is generated

Begin implementation now. Start with Phase 1.
