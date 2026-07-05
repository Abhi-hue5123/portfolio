"""
pages/05_Archive.py — Project Archive Page
JSON-driven | Uses shared utils
"""
import streamlit as st
from utils import inject_css, load_data, page_header, render_tech_badges

st.set_page_config(
    page_title="Archive — Abhiram Singuru",
    page_icon="📂",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()
page_header("Archive")

data    = load_data()
archive = data.get("archive", [])

st.markdown("""
<div class="glass-card" style="margin-bottom:28px;">
    <span class="section-label">§ 08 — Archive</span>
    <div class="section-title">Full Project History</div>
    <div class="section-desc">
        A complete, chronological record of all projects, client engagements,
        and engineering contributions across my career.
    </div>
</div>
""", unsafe_allow_html=True)

# ── Archive table ──────────────────────────────────────────────────────────────
rows_html = ""
prev_year = None

for entry in archive:
    year    = entry.get("year", "")
    project = entry.get("project", "")
    company = entry.get("company", "")
    tags    = render_tech_badges(entry.get("tech_tags", []))

    # Only print the year when it changes (grouped visual)
    year_cell = f'<span class="archive-year">{year}</span>' if year != prev_year else ""
    prev_year = year

    rows_html += f"""
    <tr>
        <td>{year_cell}</td>
        <td style="color:#e5e7eb; font-weight:500;">{project}</td>
        <td style="color:#9ca3af;">{company}</td>
        <td>{tags}</td>
    </tr>
    """

st.markdown(f"""
<div class="glass-card">
    <table class="archive-table">
        <thead>
            <tr>
                <th>Year</th>
                <th>Project</th>
                <th>Company</th>
                <th>Stack</th>
            </tr>
        </thead>
        <tbody>
            {rows_html}
        </tbody>
    </table>
</div>
""", unsafe_allow_html=True)
