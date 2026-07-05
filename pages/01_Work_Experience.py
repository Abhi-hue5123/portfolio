"""
pages/01_Work_Experience.py — Work Experience Timeline Page
JSON-driven | Uses shared utils
"""
import streamlit as st
from utils import inject_css, load_data, page_header, render_tech_badges

st.set_page_config(
    page_title="Work Experience — Abhiram Singuru",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()
page_header("Experience")

data            = load_data()
experience_list = data.get("experience", [])

st.markdown("""
<div class="glass-card" style="margin-top:10px;">
    <span class="section-label">§ 04 — Experience</span>
    <div class="section-title">Professional Experience</div>
    <div class="section-desc">
        A chronological timeline of my engineering roles, project contributions, and
        database optimizations at Cognizant Technology Solutions.
    </div>
""", unsafe_allow_html=True)

# ── Build timeline items ───────────────────────────────────────────────────────
timeline_html = '<div class="timeline-container">'

for item in experience_list:
    bullets = "".join(f"<li>{b}</li>" for b in item.get("bullet_points", []))
    tags    = render_tech_badges(item.get("tech_tags", []))
    timeline_html += f"""
    <div class="timeline-item">
        <div class="timeline-date">{item.get("date", "")}</div>
        <div class="timeline-title">{item.get("title", "")}</div>
        <div class="timeline-company">{item.get("company", "")}</div>
        <div class="timeline-content">
            <ul>{bullets}</ul>
            <div style="margin-top:12px;">{tags}</div>
        </div>
    </div>
    """

timeline_html += "</div></div>"  # close timeline-container + glass-card
st.markdown(timeline_html, unsafe_allow_html=True)