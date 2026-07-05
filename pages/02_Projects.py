"""
pages/02_Projects.py — Projects Showcase Page
JSON-driven | Uses shared utils
"""
import streamlit as st
from utils import inject_css, load_data, page_header, render_tech_badges

st.set_page_config(
    page_title="Projects — Abhiram Singuru",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()
page_header("Projects")

data     = load_data()
projects = data.get("projects", [])

st.markdown("""
<div class="glass-card" style="margin-bottom:28px;">
    <span class="section-label">§ 05 — Projects</span>
    <div class="section-title">Selected Work</div>
    <div class="section-desc">
        A curated set of personal and professional projects spanning database engineering,
        automation pipelines, full-stack services, and AI-assisted tooling.
    </div>
</div>
""", unsafe_allow_html=True)

# ── Project cards in a CSS grid ───────────────────────────────────────────────
cards_html = '<div class="project-grid">'

for p in projects:
    tags = render_tech_badges(p.get("tech_tags", []))
    cards_html += f"""
    <div class="project-card">
        <span class="category-badge">{p.get("category", "")}</span>
        <div class="project-title">{p.get("title", "")}</div>
        <div class="project-desc">{p.get("description", "")}</div>
        <div style="margin-top:auto; padding-top:12px;">{tags}</div>
    </div>
    """

cards_html += "</div>"
st.markdown(cards_html, unsafe_allow_html=True)
