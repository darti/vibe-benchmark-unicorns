# Magic Unicorn Trading Dashboard - Wireframe Specification

> This document provides a complete specification for regenerating the Magic Unicorn Trading Dashboard wireframe.

## Overview

A comprehensive dashboard application for tracking Key Performance Indicators (KPIs) related to:
- **Unicorn Population Metrics** - Census data, breed distribution, geographic spread
- **Trading Activity** - Active trades, valuations, market trends

## Dashboard Layout

### Dimensions
- **Canvas Size**: 1920 x 1080 pixels (Full HD)
- **Sidebar Width**: 280px
- **Header Height**: 80px
- **Content Padding**: 20px

### Color Palette (Wireframe Style)
| Element | Color (RGB) |
|---------|-------------|
| Background | `(248, 249, 250)` |
| Card Background | `(255, 255, 255)` |
| Border | `(200, 200, 200)` |
| Primary Text | `(60, 60, 60)` |
| Secondary Text | `(120, 120, 120)` |
| Accent (Purple) | `(180, 130, 200)` |

---

## Component Specifications

### 1. Sidebar Navigation (Left)
**Position**: `x: 0, y: 0, width: 280px, height: 100%`
**Background**: Dark `(45, 45, 55)`

#### Elements:
- **Logo Area**: "UniTrade" with unicorn emoji at top
- **Navigation Items** (vertical list):
  1. Dashboard (active state with purple accent bar)
  2. Population
  3. Trading
  4. Analytics
  5. Inventory
  6. Reports
  7. Settings
- **User Profile Section**: Bottom of sidebar with avatar, name, email

---

### 2. Header Bar (Top)
**Position**: `x: 280px, y: 0, width: remaining, height: 80px`

#### Elements:
- **Page Title**: "Magic Unicorn Dashboard" (20px bold)
- **Breadcrumb**: "Home / Dashboard / Overview"
- **Search Bar**: Rounded input with search icon (right side)
- **Action Icons**: Notifications, Messages, Settings
- **Date/Time Display**: Current date and time

---

### 3. KPI Cards Row
**Position**: Row 1 of main content
**Layout**: 4 equal-width cards with 20px gaps

| Card | Icon | Metric | Value | Change |
|------|------|--------|-------|--------|
| 1 | Unicorn | Total Population | 12,847 | +3.2% |
| 2 | Chart | Active Trades | 1,284 | +12.5% |
| 3 | Money | Avg. Trade Value | $87,420 | -2.1% |
| 4 | Sparkle | New Registrations | 342 | +8.7% |

**Card Dimensions**: `height: 90px`

---

### 4. Charts Row (Row 2)
**Height**: 280px

#### 4.1 Population Trend Line Chart
**Position**: Left 60% of row
**Title**: "Population Trend (12 Months)"

- **X-Axis**: Months (Jan - Dec)
- **Y-Axis**: Population count (0 - 100K)
- **Data Points**: 12 monthly values showing upward trend
- **Style**: Purple line with filled area below, dot markers

#### 4.2 Population by Habitat (Donut Chart)
**Position**: Right 40% of row
**Title**: "Population by Habitat"

| Segment | Percentage | Color |
|---------|------------|-------|
| Wild | 35% | `(147, 112, 219)` |
| Captive | 25% | `(180, 130, 200)` |
| Sanctuary | 20% | `(200, 160, 220)` |
| Reserve | 20% | `(220, 190, 240)` |

- **Center Display**: Total count "12.4K"

---

### 5. Visualization Row (Row 3)
**Height**: 220px

#### 5.1 Breed Popularity (Horizontal Bar Chart)
**Position**: Left 35%
**Title**: "Breed Popularity"

| Breed | Popularity |
|-------|------------|
| Rainbow | 80% |
| Celestial | 65% |
| Shadow | 50% |
| Crystal | 45% |
| Golden | 35% |

#### 5.2 Geographic Distribution (Map)
**Position**: Center 40%
**Title**: "Geographic Distribution"

- World map placeholder with hotspot markers
- **Regions with markers**:
  - EU: 3.2K
  - NA: 4.1K
  - Asia: 2.8K
  - Oceania: 1.2K
  - Africa: 1.1K

#### 5.3 Recent Activity Feed
**Position**: Right 25%
**Title**: "Recent Activity"

Timeline with entries:
```
10:42  New listing: Aurora (#0039)
10:38  Trade completed: $92,000
10:25  Bid received: Moonbeam
10:12  Price alert: Golden breed +5%
09:58  New registration: Nebula
```

---

### 6. Data Table (Row 4)
**Position**: Full width bottom section
**Title**: "Recent Listings"

| Column | Width |
|--------|-------|
| ID | 60px |
| Name | 90px |
| Breed | 80px |
| Status | 80px |
| Value | 80px |

#### Sample Data:
| ID | Name | Breed | Status | Value |
|----|------|-------|--------|-------|
| #0042 | Stardust | Celestial | Available | $84,500 |
| #0041 | Moonbeam | Rainbow | Reserved | $92,000 |
| #0040 | Twilight | Shadow | Sold | $76,800 |
| #0039 | Aurora | Crystal | Available | $88,200 |
| #0038 | Nebula | Golden | Reserved | $125,000 |

**Status Colors**:
- Available: Green `(46, 125, 50)`
- Reserved: Orange `(245, 124, 0)`
- Sold: Red `(198, 40, 40)`

---

## Regeneration Instructions

### Prerequisites
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install Pillow
```

### Generate Wireframe
```bash
python wireframes/generate_wireframe.py
```

### Output
- **File**: `wireframes/unicorn_dashboard_wireframe.png`
- **Format**: PNG, 1920x1080 pixels

---

## Design Principles

1. **Grayscale Base**: Primary wireframe uses grayscale with purple accent for unicorn theme
2. **Card-Based Layout**: All components contained in rounded-corner cards
3. **Visual Hierarchy**: KPIs at top, trends in middle, details at bottom
4. **Consistent Spacing**: 20px padding and gaps throughout
5. **Readable Typography**: Clear font sizes (10-28px range)

---

## Customization Points

To modify the wireframe, edit `generate_wireframe.py`:

| Variable | Purpose |
|----------|---------|
| `WIDTH`, `HEIGHT` | Canvas dimensions |
| `SIDEBAR_WIDTH` | Navigation width |
| `HIGHLIGHT` | Accent color (RGB tuple) |
| `data_points` in `draw_line_chart()` | Chart data |
| `segments` in `draw_donut_chart()` | Pie segments |
| `rows` in `draw_table()` | Table content |
