#!/usr/bin/env python3
"""
Magic Unicorn Trading Dashboard - Wireframe Generator
Generates a comprehensive PNG wireframe for a KPI dashboard
tracking unicorn population and trading metrics.
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Dashboard dimensions
WIDTH = 1920
HEIGHT = 1080
PADDING = 20
HEADER_HEIGHT = 80
SIDEBAR_WIDTH = 280

# Colors (grayscale wireframe style)
BG_COLOR = (248, 249, 250)
CARD_BG = (255, 255, 255)
BORDER_COLOR = (200, 200, 200)
TEXT_COLOR = (60, 60, 60)
TEXT_LIGHT = (120, 120, 120)
ACCENT_COLOR = (100, 100, 100)
CHART_LINE = (80, 80, 80)
CHART_FILL = (220, 220, 220)
HIGHLIGHT = (180, 130, 200)  # Subtle purple for unicorn theme

def get_font(size=14, bold=False):
    """Try to get a system font, fallback to default."""
    try:
        if bold:
            return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
        return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
    except:
        return ImageFont.load_default()

def draw_rounded_rect(draw, coords, radius=8, fill=None, outline=None, width=1):
    """Draw a rounded rectangle."""
    x1, y1, x2, y2 = coords
    draw.rounded_rectangle(coords, radius=radius, fill=fill, outline=outline, width=width)

def draw_card(draw, x, y, w, h, title=None):
    """Draw a card component with optional title."""
    draw_rounded_rect(draw, (x, y, x+w, y+h), radius=8, fill=CARD_BG, outline=BORDER_COLOR)
    if title:
        font = get_font(14, bold=True)
        draw.text((x + 16, y + 12), title, fill=TEXT_COLOR, font=font)
        draw.line((x, y + 40, x + w, y + 40), fill=BORDER_COLOR, width=1)
    return y + 48 if title else y + 12

def draw_kpi_card(draw, x, y, w, h, label, value, change=None, icon="◆"):
    """Draw a KPI metric card."""
    draw_card(draw, x, y, w, h)

    # Icon placeholder
    font_icon = get_font(24)
    draw.text((x + 16, y + 20), icon, fill=HIGHLIGHT, font=font_icon)

    # Value
    font_value = get_font(28, bold=True)
    draw.text((x + 50, y + 16), value, fill=TEXT_COLOR, font=font_value)

    # Label
    font_label = get_font(12)
    draw.text((x + 50, y + 50), label, fill=TEXT_LIGHT, font=font_label)

    # Change indicator
    if change:
        change_color = (46, 125, 50) if change.startswith("+") else (198, 40, 40)
        draw.text((x + w - 60, y + 20), change, fill=change_color, font=font_label)

def draw_line_chart(draw, x, y, w, h, title, data_points=None):
    """Draw a line chart placeholder."""
    content_y = draw_card(draw, x, y, w, h, title)

    chart_x = x + 40
    chart_y = content_y + 10
    chart_w = w - 60
    chart_h = h - 80

    # Axes
    draw.line((chart_x, chart_y, chart_x, chart_y + chart_h), fill=BORDER_COLOR, width=1)
    draw.line((chart_x, chart_y + chart_h, chart_x + chart_w, chart_y + chart_h), fill=BORDER_COLOR, width=1)

    # Y-axis labels
    font_small = get_font(10)
    for i, label in enumerate(["100K", "75K", "50K", "25K", "0"]):
        ly = chart_y + (chart_h * i // 4)
        draw.text((chart_x - 35, ly - 5), label, fill=TEXT_LIGHT, font=font_small)
        draw.line((chart_x, ly, chart_x + chart_w, ly), fill=(240, 240, 240), width=1)

    # X-axis labels
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for i, month in enumerate(months):
        lx = chart_x + (chart_w * i // 11)
        draw.text((lx - 10, chart_y + chart_h + 8), month, fill=TEXT_LIGHT, font=font_small)

    # Sample line data
    if data_points is None:
        data_points = [0.3, 0.35, 0.4, 0.38, 0.5, 0.55, 0.52, 0.6, 0.65, 0.7, 0.68, 0.75]

    points = []
    for i, val in enumerate(data_points):
        px = chart_x + (chart_w * i // (len(data_points) - 1))
        py = chart_y + chart_h - int(chart_h * val)
        points.append((px, py))

    # Fill under line
    fill_points = points + [(points[-1][0], chart_y + chart_h), (points[0][0], chart_y + chart_h)]
    draw.polygon(fill_points, fill=(HIGHLIGHT[0], HIGHLIGHT[1], HIGHLIGHT[2], 50))

    # Draw line
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=HIGHLIGHT, width=2)

    # Draw points
    for px, py in points:
        draw.ellipse((px-4, py-4, px+4, py+4), fill=HIGHLIGHT, outline=CARD_BG, width=2)

def draw_bar_chart(draw, x, y, w, h, title, labels=None, values=None):
    """Draw a bar chart placeholder."""
    content_y = draw_card(draw, x, y, w, h, title)

    if labels is None:
        labels = ["Rainbow", "Celestial", "Shadow", "Crystal", "Golden"]
    if values is None:
        values = [0.8, 0.65, 0.5, 0.45, 0.35]

    bar_area_y = content_y + 10
    bar_height = 28
    bar_spacing = 8
    max_bar_width = w - 120

    font_small = get_font(11)

    for i, (label, val) in enumerate(zip(labels, values)):
        by = bar_area_y + i * (bar_height + bar_spacing)

        # Label
        draw.text((x + 16, by + 6), label, fill=TEXT_COLOR, font=font_small)

        # Bar background
        bar_x = x + 90
        draw.rounded_rectangle((bar_x, by, bar_x + max_bar_width, by + bar_height),
                               radius=4, fill=CHART_FILL)

        # Bar fill
        bar_fill_w = int(max_bar_width * val)
        draw.rounded_rectangle((bar_x, by, bar_x + bar_fill_w, by + bar_height),
                               radius=4, fill=HIGHLIGHT)

        # Value
        draw.text((bar_x + max_bar_width + 8, by + 6), f"{int(val*100)}%", fill=TEXT_LIGHT, font=font_small)

def draw_donut_chart(draw, x, y, w, h, title, segments=None):
    """Draw a donut/pie chart placeholder."""
    content_y = draw_card(draw, x, y, w, h, title)

    center_x = x + w // 3
    center_y = content_y + (h - 60) // 2
    outer_r = min(w // 3, (h - 60) // 2) - 20
    inner_r = outer_r - 25

    if segments is None:
        segments = [
            ("Wild", 0.35, (147, 112, 219)),
            ("Captive", 0.25, (180, 130, 200)),
            ("Sanctuary", 0.20, (200, 160, 220)),
            ("Reserve", 0.20, (220, 190, 240))
        ]

    # Draw segments (simplified as arcs)
    start_angle = 0
    for name, pct, color in segments:
        end_angle = start_angle + int(360 * pct)
        draw.pieslice((center_x - outer_r, center_y - outer_r,
                       center_x + outer_r, center_y + outer_r),
                      start=start_angle, end=end_angle, fill=color)
        start_angle = end_angle

    # Inner circle (donut hole)
    draw.ellipse((center_x - inner_r, center_y - inner_r,
                  center_x + inner_r, center_y + inner_r), fill=CARD_BG)

    # Center text
    font_center = get_font(20, bold=True)
    font_small = get_font(10)
    draw.text((center_x - 25, center_y - 15), "12.4K", fill=TEXT_COLOR, font=font_center)
    draw.text((center_x - 15, center_y + 10), "Total", fill=TEXT_LIGHT, font=font_small)

    # Legend
    legend_x = x + w // 2 + 20
    legend_y = content_y + 20
    font_legend = get_font(11)

    for i, (name, pct, color) in enumerate(segments):
        ly = legend_y + i * 28
        draw.rectangle((legend_x, ly, legend_x + 12, ly + 12), fill=color)
        draw.text((legend_x + 20, ly - 2), f"{name} ({int(pct*100)}%)", fill=TEXT_COLOR, font=font_legend)

def draw_table(draw, x, y, w, h, title, headers=None, rows=None):
    """Draw a data table placeholder."""
    content_y = draw_card(draw, x, y, w, h, title)

    if headers is None:
        headers = ["ID", "Name", "Breed", "Status", "Value"]
    if rows is None:
        rows = [
            ["#0042", "Stardust", "Celestial", "Available", "$84,500"],
            ["#0041", "Moonbeam", "Rainbow", "Reserved", "$92,000"],
            ["#0040", "Twilight", "Shadow", "Sold", "$76,800"],
            ["#0039", "Aurora", "Crystal", "Available", "$88,200"],
            ["#0038", "Nebula", "Golden", "Reserved", "$125,000"],
        ]

    font_header = get_font(11, bold=True)
    font_cell = get_font(11)

    col_widths = [60, 90, 80, 80, 80]
    row_height = 32

    # Header row
    hx = x + 16
    for i, header in enumerate(headers):
        draw.text((hx, content_y + 5), header, fill=TEXT_LIGHT, font=font_header)
        hx += col_widths[i]

    draw.line((x + 10, content_y + 25, x + w - 10, content_y + 25), fill=BORDER_COLOR)

    # Data rows
    for ri, row in enumerate(rows):
        ry = content_y + 35 + ri * row_height
        rx = x + 16

        # Alternating row background
        if ri % 2 == 1:
            draw.rectangle((x + 5, ry - 5, x + w - 5, ry + row_height - 10), fill=(250, 250, 250))

        for ci, cell in enumerate(row):
            color = TEXT_COLOR
            if cell == "Available":
                color = (46, 125, 50)
            elif cell == "Reserved":
                color = (245, 124, 0)
            elif cell == "Sold":
                color = (198, 40, 40)
            draw.text((rx, ry), cell, fill=color, font=font_cell)
            rx += col_widths[ci]

def draw_map_placeholder(draw, x, y, w, h, title):
    """Draw a map placeholder for geographic distribution."""
    content_y = draw_card(draw, x, y, w, h, title)

    # Map area
    map_x = x + 16
    map_y = content_y + 10
    map_w = w - 32
    map_h = h - 80

    draw.rounded_rectangle((map_x, map_y, map_x + map_w, map_y + map_h),
                           radius=4, fill=(240, 242, 245), outline=BORDER_COLOR)

    # Simplified world map outline (very abstract)
    font_map = get_font(12)
    draw.text((map_x + map_w // 2 - 40, map_y + map_h // 2 - 10),
              "[World Map]", fill=TEXT_LIGHT, font=font_map)

    # Hotspot markers
    hotspots = [
        (0.2, 0.3, "EU: 3.2K"),
        (0.15, 0.5, "NA: 4.1K"),
        (0.7, 0.4, "Asia: 2.8K"),
        (0.8, 0.7, "Oceania: 1.2K"),
        (0.4, 0.6, "Africa: 1.1K")
    ]

    font_small = get_font(9)
    for px, py, label in hotspots:
        hx = map_x + int(map_w * px)
        hy = map_y + int(map_h * py)
        draw.ellipse((hx - 8, hy - 8, hx + 8, hy + 8), fill=HIGHLIGHT, outline=CARD_BG, width=2)
        draw.text((hx + 12, hy - 5), label, fill=TEXT_COLOR, font=font_small)

def draw_activity_feed(draw, x, y, w, h, title):
    """Draw an activity feed/timeline."""
    content_y = draw_card(draw, x, y, w, h, title)

    activities = [
        ("10:42", "New listing: Aurora (#0039)", "●"),
        ("10:38", "Trade completed: $92,000", "◆"),
        ("10:25", "Bid received: Moonbeam", "▲"),
        ("10:12", "Price alert: Golden breed +5%", "!"),
        ("09:58", "New registration: Nebula", "●"),
    ]

    font_time = get_font(10)
    font_activity = get_font(11)

    for i, (time, text, icon) in enumerate(activities):
        ay = content_y + 10 + i * 32

        # Timeline dot
        draw.ellipse((x + 20, ay + 4, x + 28, ay + 12), fill=HIGHLIGHT)
        if i < len(activities) - 1:
            draw.line((x + 24, ay + 14, x + 24, ay + 32), fill=BORDER_COLOR, width=1)

        # Time
        draw.text((x + 36, ay), time, fill=TEXT_LIGHT, font=font_time)

        # Activity text
        draw.text((x + 80, ay), text, fill=TEXT_COLOR, font=font_activity)

def draw_sidebar(draw, x, y, w, h):
    """Draw the sidebar navigation."""
    draw.rectangle((x, y, x + w, y + h), fill=(45, 45, 55))

    # Logo area
    font_logo = get_font(18, bold=True)
    draw.text((x + 20, y + 25), "🦄 UniTrade", fill=(255, 255, 255), font=font_logo)
    draw.line((x, y + 70, x + w, y + 70), fill=(60, 60, 70), width=1)

    # Navigation items
    nav_items = [
        ("◈", "Dashboard", True),
        ("◇", "Population", False),
        ("◆", "Trading", False),
        ("○", "Analytics", False),
        ("□", "Inventory", False),
        ("△", "Reports", False),
        ("☆", "Settings", False),
    ]

    font_nav = get_font(13)
    nav_y = y + 90

    for icon, label, active in nav_items:
        if active:
            draw.rectangle((x, nav_y - 5, x + w, nav_y + 30), fill=(60, 60, 75))
            draw.rectangle((x, nav_y - 5, x + 4, nav_y + 30), fill=HIGHLIGHT)

        draw.text((x + 24, nav_y), icon, fill=(200, 200, 200) if not active else (255, 255, 255), font=font_nav)
        draw.text((x + 50, nav_y), label, fill=(180, 180, 180) if not active else (255, 255, 255), font=font_nav)
        nav_y += 45

    # User section at bottom
    draw.line((x, y + h - 70, x + w, y + h - 70), fill=(60, 60, 70), width=1)
    draw.ellipse((x + 20, y + h - 50, x + 45, y + h - 25), fill=(100, 100, 120))
    font_user = get_font(12)
    draw.text((x + 55, y + h - 48), "Admin User", fill=(220, 220, 220), font=font_user)
    draw.text((x + 55, y + h - 32), "admin@unitrade.io", fill=(140, 140, 140), font=get_font(10))

def draw_header(draw, x, y, w, h):
    """Draw the top header bar."""
    draw.rectangle((x, y, x + w, y + h), fill=CARD_BG, outline=BORDER_COLOR)

    # Page title
    font_title = get_font(20, bold=True)
    draw.text((x + 20, y + 25), "Magic Unicorn Dashboard", fill=TEXT_COLOR, font=font_title)

    # Breadcrumb
    font_small = get_font(11)
    draw.text((x + 20, y + 55), "Home / Dashboard / Overview", fill=TEXT_LIGHT, font=font_small)

    # Search bar
    search_x = x + w - 400
    draw_rounded_rect(draw, (search_x, y + 20, search_x + 200, y + 50), radius=20, fill=BG_COLOR, outline=BORDER_COLOR)
    draw.text((search_x + 15, y + 28), "🔍 Search...", fill=TEXT_LIGHT, font=font_small)

    # Notification icons
    icon_x = x + w - 150
    font_icon = get_font(16)
    draw.text((icon_x, y + 28), "🔔", font=font_icon)
    draw.text((icon_x + 35, y + 28), "💬", font=font_icon)
    draw.text((icon_x + 70, y + 28), "⚙️", font=font_icon)

    # Date/time
    draw.text((x + w - 180, y + 55), "Jan 2, 2026 • 10:45 AM", fill=TEXT_LIGHT, font=font_small)

def main():
    # Create image
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Draw sidebar
    draw_sidebar(draw, 0, 0, SIDEBAR_WIDTH, HEIGHT)

    # Draw header
    content_x = SIDEBAR_WIDTH
    draw_header(draw, content_x, 0, WIDTH - SIDEBAR_WIDTH, HEADER_HEIGHT)

    # Main content area
    main_x = content_x + PADDING
    main_y = HEADER_HEIGHT + PADDING
    main_w = WIDTH - SIDEBAR_WIDTH - (PADDING * 2)

    # Row 1: KPI Cards
    kpi_width = (main_w - 60) // 4
    kpi_height = 90

    draw_kpi_card(draw, main_x, main_y, kpi_width, kpi_height,
                  "Total Population", "12,847", "+3.2%", "🦄")
    draw_kpi_card(draw, main_x + kpi_width + 20, main_y, kpi_width, kpi_height,
                  "Active Trades", "1,284", "+12.5%", "📈")
    draw_kpi_card(draw, main_x + (kpi_width + 20) * 2, main_y, kpi_width, kpi_height,
                  "Avg. Trade Value", "$87,420", "-2.1%", "💰")
    draw_kpi_card(draw, main_x + (kpi_width + 20) * 3, main_y, kpi_width, kpi_height,
                  "New Registrations", "342", "+8.7%", "✨")

    # Row 2: Charts
    row2_y = main_y + kpi_height + PADDING
    chart_height = 280

    # Population trend chart (larger)
    draw_line_chart(draw, main_x, row2_y, int(main_w * 0.6) - 10, chart_height,
                   "Population Trend (12 Months)")

    # Breed distribution donut
    draw_donut_chart(draw, main_x + int(main_w * 0.6) + 10, row2_y,
                    int(main_w * 0.4) - 10, chart_height,
                    "Population by Habitat")

    # Row 3: More visualizations
    row3_y = row2_y + chart_height + PADDING
    row3_height = 220

    # Breed popularity bar chart
    draw_bar_chart(draw, main_x, row3_y, int(main_w * 0.35) - 10, row3_height,
                  "Breed Popularity")

    # Geographic distribution map
    draw_map_placeholder(draw, main_x + int(main_w * 0.35) + 10, row3_y,
                        int(main_w * 0.4) - 10, row3_height,
                        "Geographic Distribution")

    # Activity feed
    draw_activity_feed(draw, main_x + int(main_w * 0.75) + 10, row3_y,
                      int(main_w * 0.25) - 10, row3_height,
                      "Recent Activity")

    # Row 4: Data table
    row4_y = row3_y + row3_height + PADDING
    row4_height = HEIGHT - row4_y - PADDING

    draw_table(draw, main_x, row4_y, main_w, row4_height,
              "Recent Listings")

    # Save the image
    output_path = os.path.join(os.path.dirname(__file__), "unicorn_dashboard_wireframe.png")
    img.save(output_path, "PNG", quality=95)
    print(f"Wireframe saved to: {output_path}")

    return output_path

if __name__ == "__main__":
    main()
