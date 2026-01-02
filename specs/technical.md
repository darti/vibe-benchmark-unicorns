# Technical Specification

> This document defines the technical foundation for the Magic Unicorn Trading Dashboard application. It serves as authoritative guidance for implementation decisions.

---

## Application Architecture

### Type: Single Page Application (SPA)

The application is a client-side rendered SPA. All routing, state management, and view rendering occur in the browser.

**Key characteristics:**
- One HTML entry point (`index.html`)
- Client-side routing (no full page reloads)
- API communication via async HTTP requests
- Browser history management for navigation

---

## Technology Stack

### Core Framework: Vue 3 with Composition API

Use Vue 3 exclusively with the Composition API pattern. Do not use the Options API.

**Required patterns:**

```typescript
// ✓ CORRECT: Composition API with <script setup>
<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'

const count = ref(0)
const doubled = computed(() => count.value * 2)

onMounted(() => {
  // initialization logic
})
</script>
```

```typescript
// ✗ INCORRECT: Options API - do not use
export default {
  data() { return { count: 0 } },
  computed: { doubled() { return this.count * 2 } }
}
```

**Composables for reusable logic:**

Extract shared stateful logic into composables (functions prefixed with `use`):

```typescript
// composables/useUnicornPopulation.ts
export function useUnicornPopulation() {
  const population = ref<number>(0)
  const isLoading = ref(false)
  
  async function fetchPopulation() {
    isLoading.value = true
    // ... fetch logic
    isLoading.value = false
  }
  
  return { population, isLoading, fetchPopulation }
}
```

---

### Language: TypeScript

All code must be written in TypeScript with strict mode enabled.

**Configuration requirements:**

```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true
  }
}
```

**Type definitions:**

- Define explicit interfaces for all data structures
- Use type inference where types are obvious
- Avoid `any` - use `unknown` with type guards when type is truly unknown

```typescript
// ✓ CORRECT: Explicit interface
interface Unicorn {
  id: string
  name: string
  breed: UnicornBreed
  status: 'available' | 'reserved' | 'sold'
  value: number
}

// ✓ CORRECT: Type inference for obvious cases
const count = ref(0) // inferred as Ref<number>

// ✗ INCORRECT: Using any
const data: any = fetchData()
```

---

### Component Library: PrimeVue

Use PrimeVue as the component library. Import components individually for optimal bundle size.

**Setup pattern:**

```typescript
// main.ts
import PrimeVue from 'primevue/config'
import Aura from '@primevue/themes/aura'

app.use(PrimeVue, {
  theme: {
    preset: Aura,
    options: {
      darkModeSelector: '.dark-mode'
    }
  }
})
```

**Component usage:**

```vue
<script setup lang="ts">
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import Card from 'primevue/card'
import Chart from 'primevue/chart'
</script>

<template>
  <Card>
    <template #content>
      <DataTable :value="unicorns">
        <Column field="name" header="Name" />
        <Column field="breed" header="Breed" />
      </DataTable>
    </template>
  </Card>
</template>
```

**Preferred PrimeVue components by use case:**

| Use Case | Component |
|----------|-----------|
| Data tables | `DataTable`, `Column` |
| Charts | `Chart` (Chart.js wrapper) |
| Cards/Containers | `Card`, `Panel` |
| Navigation | `Menu`, `Menubar`, `PanelMenu` |
| Forms | `InputText`, `Select`, `Button` |
| Feedback | `Toast`, `Message`, `ProgressSpinner` |

---

### End-to-End Testing

Use Playwright for E2E testing.

**Test file structure:**

```
tests/
  e2e/
    dashboard.spec.ts
    trading.spec.ts
    navigation.spec.ts
```

**Test patterns:**

```typescript
import { test, expect } from '@playwright/test'

test.describe('Dashboard', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/')
  })

  test('displays KPI cards', async ({ page }) => {
    await expect(page.getByTestId('kpi-population')).toBeVisible()
    await expect(page.getByTestId('kpi-trades')).toBeVisible()
  })

  test('navigates to trading page', async ({ page }) => {
    await page.getByRole('link', { name: 'Trading' }).click()
    await expect(page).toHaveURL('/trading')
  })
})
```

**Test attributes:**

Add `data-testid` attributes for test selectors:

```vue
<template>
  <Card data-testid="kpi-population">
    <!-- content -->
  </Card>
</template>
```

---

## Project Structure

```
src/
  assets/            # Static assets (images, fonts)
  components/        # Reusable Vue components
    common/          # Generic components (buttons, inputs)
    charts/          # Chart components
    layout/          # Layout components (sidebar, header)
  composables/       # Composition API hooks
  router/            # Vue Router configuration
  services/          # API clients and external integrations
  stores/            # Pinia state stores
  types/             # TypeScript type definitions
  views/             # Page-level components
  App.vue            # Root component
  main.ts            # Application entry point
tests/
  e2e/               # Playwright E2E tests
  unit/              # Vitest unit tests
```

---

## Design Principles

### 1. Single Responsibility

Each component, composable, and function should do one thing well.

```typescript
// ✓ CORRECT: Single responsibility
function formatCurrency(value: number): string {
  return new Intl.NumberFormat('en-US', { 
    style: 'currency', 
    currency: 'USD' 
  }).format(value)
}

// ✗ INCORRECT: Multiple responsibilities
function formatAndValidateAndSaveCurrency(value: number) {
  // formatting + validation + API call = too much
}
```

### 2. Composition Over Inheritance

Build complex behavior by combining simple composables, not through inheritance hierarchies.

```typescript
// ✓ CORRECT: Composing behaviors
function useUnicornDetails(id: Ref<string>) {
  const { data, isLoading, error } = useFetch(`/api/unicorns/${id.value}`)
  const { format } = useCurrencyFormatter()
  
  const formattedValue = computed(() => 
    data.value ? format(data.value.value) : null
  )
  
  return { data, isLoading, error, formattedValue }
}
```

### 3. Explicit Over Implicit

Prefer explicit declarations that make code self-documenting.

```typescript
// ✓ CORRECT: Explicit props with defaults
const props = withDefaults(defineProps<{
  title: string
  value: number
  trend?: 'up' | 'down' | 'neutral'
}>(), {
  trend: 'neutral'
})

// ✓ CORRECT: Explicit emits
const emit = defineEmits<{
  (e: 'update', value: number): void
  (e: 'delete', id: string): void
}>()
```

### 4. Colocation

Keep related code together. Tests near source, types near usage.

```
components/
  KpiCard/
    KpiCard.vue
    KpiCard.spec.ts    # Unit test colocated
    types.ts           # Component-specific types
```

### 5. Fail Fast, Fail Loudly

Validate inputs early and throw meaningful errors.

```typescript
function calculateGrowth(current: number, previous: number): number {
  if (previous === 0) {
    throw new Error('Cannot calculate growth: previous value is zero')
  }
  return ((current - previous) / previous) * 100
}
```

### 6. Immutability by Default

Avoid mutating data. Create new objects/arrays instead.

```typescript
// ✓ CORRECT: Immutable update
const updatedUnicorns = unicorns.value.map(u => 
  u.id === id ? { ...u, status: 'sold' } : u
)

// ✗ INCORRECT: Mutation
unicorns.value.find(u => u.id === id).status = 'sold'
```

### 7. Meaningful Names

Names should reveal intent. Avoid abbreviations except for well-known terms.

```typescript
// ✓ CORRECT: Clear intent
const isPopulationLoading = ref(false)
const fetchUnicornsByBreed = async (breed: string) => { }

// ✗ INCORRECT: Cryptic abbreviations  
const isPL = ref(false)
const fetchUBB = async (b: string) => { }
```

---

## State Management Guidelines

Use Pinia for global state. Keep state minimal and derived data in computed properties.

```typescript
// stores/unicorns.ts
export const useUnicornStore = defineStore('unicorns', () => {
  // State
  const unicorns = ref<Unicorn[]>([])
  const selectedBreed = ref<string | null>(null)
  
  // Derived state (computed)
  const filteredUnicorns = computed(() => 
    selectedBreed.value 
      ? unicorns.value.filter(u => u.breed === selectedBreed.value)
      : unicorns.value
  )
  
  const totalValue = computed(() =>
    unicorns.value.reduce((sum, u) => sum + u.value, 0)
  )
  
  // Actions
  async function fetchAll() {
    unicorns.value = await unicornService.getAll()
  }
  
  return { 
    unicorns, 
    selectedBreed, 
    filteredUnicorns, 
    totalValue, 
    fetchAll 
  }
})
```

**When to use Pinia vs local state:**

| Scenario | Solution |
|----------|----------|
| UI state (open/closed, hover) | Local `ref()` |
| Form data | Local `ref()` or `reactive()` |
| Data shared across routes | Pinia store |
| Data fetched from API | Pinia store |
| Derived from multiple sources | Pinia computed |

---

## API Integration Pattern

Create typed service modules for API communication.

```typescript
// services/unicornService.ts
import type { Unicorn, CreateUnicornDto } from '@/types'

const BASE_URL = '/api/unicorns'

export const unicornService = {
  async getAll(): Promise<Unicorn[]> {
    const response = await fetch(BASE_URL)
    if (!response.ok) throw new ApiError(response)
    return response.json()
  },
  
  async getById(id: string): Promise<Unicorn> {
    const response = await fetch(`${BASE_URL}/${id}`)
    if (!response.ok) throw new ApiError(response)
    return response.json()
  },
  
  async create(dto: CreateUnicornDto): Promise<Unicorn> {
    const response = await fetch(BASE_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dto)
    })
    if (!response.ok) throw new ApiError(response)
    return response.json()
  }
}
```

---

## Error Handling

Handle errors at appropriate boundaries with user-friendly feedback.

```typescript
// Composable with error handling
export function useAsyncData<T>(fetcher: () => Promise<T>) {
  const data = ref<T | null>(null)
  const error = ref<Error | null>(null)
  const isLoading = ref(false)
  
  async function execute() {
    isLoading.value = true
    error.value = null
    try {
      data.value = await fetcher()
    } catch (e) {
      error.value = e instanceof Error ? e : new Error(String(e))
    } finally {
      isLoading.value = false
    }
  }
  
  return { data, error, isLoading, execute }
}
```

```vue
<!-- Component with error display -->
<template>
  <div v-if="error" class="error-state">
    <Message severity="error">
      Failed to load data. Please try again.
    </Message>
    <Button @click="retry">Retry</Button>
  </div>
  <ProgressSpinner v-else-if="isLoading" />
  <div v-else>
    <!-- content -->
  </div>
</template>
```

---

## Performance Guidelines

1. **Lazy load routes** - Split code by route for smaller initial bundle
2. **Use `v-once`** - For static content that never changes
3. **Use `v-memo`** - For expensive list rendering with known dependencies
4. **Debounce user input** - For search, filters, and other frequent updates
5. **Virtual scrolling** - For large data tables (PrimeVue DataTable supports this)

```typescript
// Lazy loaded routes
const routes = [
  { path: '/', component: () => import('@/views/Dashboard.vue') },
  { path: '/trading', component: () => import('@/views/Trading.vue') },
]
```

---

## Summary Checklist

Before implementing any feature, verify:

- [ ] Using Composition API with `<script setup>`
- [ ] TypeScript strict mode with explicit types
- [ ] PrimeVue components for UI elements
- [ ] Composables for reusable logic
- [ ] Pinia for shared state
- [ ] `data-testid` attributes for testable elements
- [ ] Error states handled with user feedback
- [ ] No `any` types
- [ ] Meaningful names throughout
