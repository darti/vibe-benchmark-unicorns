# Claude Code Instructions

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

## Claude-Specific Tips

- Use parallel tool calls for independent file operations
- Track progress with todo lists for complex phases
- Read all spec files before starting implementation
- Generate a benchmark report at session end
