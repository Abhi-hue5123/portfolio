"""
pages/03_Writing.py — Writing & Articles Page
JSON-driven | Uses shared utils
"""
import streamlit as st
from utils import inject_css, load_data, page_header

st.set_page_config(
    page_title="Writing — Abhiram Singuru",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()
page_header("Writing")

data    = load_data()
writing = data.get("writing", [])

st.markdown("""
<div class="glass-card" style="margin-bottom:28px;">
    <span class="section-label">§ 06 — Writing</span>
    <div class="section-title">Articles &amp; Tutorials</div>
    <div class="section-desc">
        Technical deep-dives, walkthroughs, and guides on Oracle databases,
        Unix automation, and cloud engineering.
    </div>
</div>
""", unsafe_allow_html=True)

# ── Writing cards ──────────────────────────────────────────────────────────────
for article in writing:
    link_href = article.get("link", "#")
    read_link = (
        f'<a class="read-link" href="{link_href}" target="_blank" rel="noopener">'
        'Read article →</a>'
        if link_href and link_href != "#"
        else '<span class="read-link" style="opacity:0.4; cursor:default;">Coming soon</span>'
    )

    st.markdown(f"""
    <div class="writing-card">
        <div style="flex:1;">
            <span class="category-badge">{article.get("category", "")}</span>
            <div class="writing-title">{article.get("title", "")}</div>
            <div class="writing-desc">{article.get("description", "")}</div>
            {read_link}
        </div>
        <div class="writing-date">{article.get("date", "")}</div>
    </div>
    """, unsafe_allow_html=True)
