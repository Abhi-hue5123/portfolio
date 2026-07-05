"""
pages/04_Uses.py — Tools & Setup Page
JSON-driven | Uses shared utils
"""
import streamlit as st
from utils import inject_css, load_data, page_header

st.set_page_config(
    page_title="Uses — Abhiram Singuru",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()
page_header("Uses")

data = load_data()
uses = data.get("uses", [])

st.markdown("""
<div class="glass-card" style="margin-bottom:28px;">
    <span class="section-label">§ 07 — Uses</span>
    <div class="section-title">Tools &amp; Setup</div>
    <div class="section-desc">
        Software, hardware, and services powering my daily development
        and database engineering workflow.
    </div>
</div>
""", unsafe_allow_html=True)

# ── Render each category as a card ────────────────────────────────────────────
for category in uses:
    items_html = "".join(
        f'<div class="uses-item">{item}</div>'
        for item in category.get("items", [])
    )
    st.markdown(f"""
    <div class="glass-card">
        <div class="uses-category-title">{category.get("category", "")}</div>
        {items_html}
    </div>
    """, unsafe_allow_html=True)
