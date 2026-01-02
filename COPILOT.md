# GitHub Copilot Instructions

This is a benchmark project for evaluating AI coding assistants.

**Your task**: Build the Magic Unicorn Trading Dashboard - a Vue 3 SPA with charts, data tables, and KPI cards.

## CRITICAL: Output Locations

- **Application code**: Must be generated inside the `generated/` folder
- **Benchmark report**: Must be created in the `benchmarks/` folder (project root)

See [AGENT.md](./AGENT.md) for complete implementation instructions.

## Quick Reference

- **Package manager**: pnpm (not npm or yarn)
- **Framework**: Vue 3 with Composition API
- **UI Library**: PrimeVue with Aura theme
- **Language**: TypeScript (strict mode)
- **Testing**: Playwright E2E tests

## Copilot-Specific Tips

- Follow the 11-phase implementation sequence
- Use inline suggestions for boilerplate code
- Verify TypeScript types are properly inferred
- Generate a benchmark report at session end
