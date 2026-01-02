# Benchmark Protocol

> **MANDATORY**: Every LLM implementation session MUST generate a benchmark report. This is not optional.

---

## Purpose

This project evaluates LLM performance on real-world coding tasks. Each implementation session produces a benchmark file that captures metrics for comparison.

---

## Benchmark File Requirements

### Location and Naming

```
benchmarks/
  {timestamp}_{model_provider}_{model_id}.md
```

**Naming convention:**
- `timestamp`: ISO 8601 format, file-safe: `YYYY-MM-DDTHH-MM-SS`
- `model_provider`: lowercase, no spaces (e.g., `anthropic`, `openai`, `google`)
- `model_id`: model identifier, lowercase (e.g., `claude-opus-4-5`, `gpt-4o`, `gemini-2-flash`)

**Example filenames:**
```
benchmarks/2025-01-15T14-32-00_anthropic_claude-opus-4-5.md
benchmarks/2025-01-15T09-15-30_openai_gpt-4o.md
```

---

## Mandatory Template

Every benchmark file MUST use this exact template. All fields are required.

````markdown
# Benchmark Report

## Session Metadata

| Field | Value |
|-------|-------|
| **Timestamp** | {ISO 8601 datetime with timezone} |
| **Model Provider** | {provider name} |
| **Model ID** | {exact model identifier used} |
| **Model Version** | {version string if available, otherwise "N/A"} |

## Token Usage

| Metric | Count |
|--------|-------|
| **Input Tokens** | {number} |
| **Output Tokens** | {number} |
| **Total Tokens** | {input + output} |

## Timing

| Metric | Value |
|--------|-------|
| **Session Start** | {ISO 8601 datetime} |
| **Session End** | {ISO 8601 datetime} |
| **Total Duration** | {duration in format: Xh Ym Zs} |

## Task Completion

| Task | Status | Notes |
|------|--------|-------|
| {task description} | ✅ Complete / ⚠️ Partial / ❌ Failed | {optional notes} |

## Files Generated

```
{list all files created or modified, one per line}
```

## Observations

{Free-form notes about the implementation process, challenges encountered, or notable behaviors}
````

---

## Field Specifications

### Model Provider

Use the canonical provider name:

| Provider | Value |
|----------|-------|
| Anthropic | `Anthropic` |
| OpenAI | `OpenAI` |
| Google | `Google` |
| Mistral | `Mistral` |
| Meta | `Meta` |
| Other | Use official company name |

### Model ID

Use the exact API model identifier:

| Example Models | Model ID |
|----------------|----------|
| Claude Opus 4.5 | `claude-opus-4-5-20251101` |
| Claude Sonnet 4 | `claude-sonnet-4-20250514` |
| GPT-4o | `gpt-4o-2024-11-20` |
| Gemini 2.0 Flash | `gemini-2.0-flash` |

### Token Counts

- Report exact counts from API response metadata
- If token counts unavailable, estimate and note: `{number} (estimated)`

### Duration Calculation

Calculate from first user message to final assistant response:
- Format: `Xh Ym Zs` (e.g., `0h 23m 45s`)
- For sessions under 1 hour: `23m 45s`
- For sessions under 1 minute: `45s`

### Task Status

| Status | Meaning |
|--------|---------|
| ✅ Complete | Task fully implemented and working |
| ⚠️ Partial | Task partially completed, some elements missing |
| ❌ Failed | Task not completed or broken |

---

## Validation Checklist

Before finalizing a benchmark file, verify:

- [ ] File is in `benchmarks/` directory
- [ ] Filename follows naming convention
- [ ] All metadata fields populated
- [ ] Token counts recorded
- [ ] Start and end times recorded
- [ ] Duration calculated correctly
- [ ] All tasks listed with status
- [ ] All generated files listed

---

## Example Benchmark File

```markdown
# Benchmark Report

## Session Metadata

| Field | Value |
|-------|-------|
| **Timestamp** | 2025-01-15T14:32:00+01:00 |
| **Model Provider** | Anthropic |
| **Model ID** | claude-opus-4-5-20251101 |
| **Model Version** | claude-opus-4-5-20251101 |

## Token Usage

| Metric | Count |
|--------|-------|
| **Input Tokens** | 12,847 |
| **Output Tokens** | 8,234 |
| **Total Tokens** | 21,081 |

## Timing

| Metric | Value |
|--------|-------|
| **Session Start** | 2025-01-15T14:00:00+01:00 |
| **Session End** | 2025-01-15T14:32:00+01:00 |
| **Total Duration** | 32m 0s |

## Task Completion

| Task | Status | Notes |
|------|--------|-------|
| Create project structure | ✅ Complete | |
| Implement Dashboard view | ✅ Complete | |
| Add KPI cards component | ✅ Complete | |
| Implement charts | ⚠️ Partial | Donut chart pending |
| Write E2E tests | ❌ Failed | Ran out of context |

## Files Generated

```
src/main.ts
src/App.vue
src/views/Dashboard.vue
src/components/KpiCard.vue
src/components/charts/LineChart.vue
src/stores/unicorns.ts
src/types/index.ts
```

## Observations

- Model handled Vue 3 Composition API patterns correctly
- Required clarification on PrimeVue Chart component syntax
- Performance degraded in final 20% of session (longer response times)
```

---

## Enforcement

**This benchmark protocol is mandatory.** 

At the end of every implementation session:

1. Create the `benchmarks/` directory if it doesn't exist
2. Generate the benchmark file using the template above
3. Populate ALL required fields
4. Verify against the validation checklist

Failure to generate a benchmark file invalidates the implementation session for comparison purposes.
