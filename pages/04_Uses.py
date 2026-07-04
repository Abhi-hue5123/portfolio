import streamlit as st
import os
import json

# Page configs (tab title, favicon)
st.set_page_config(
    page_title="Abhiram Singuru's Setup",
    page_icon="💻",
    layout="wide",
)

def load_portfolio_data():
    try:
        with open("portfolio_data.json", "r") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading portfolio_data.json: {e}")
        return {}

def uses():
    # Load JSON data
    data = load_portfolio_data()
    uses_list = data.get("uses", [])

    # Injects the glowing spotlights into the background
    st.markdown('<div class="glow-spotlight-1"></div><div class="glow-spotlight-2"></div>', unsafe_allow_html=True)

    # CSS styles file
    if os.path.exists("styles/main.css"):
        with open("styles/main.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Header / Navigation logotype mockup
    st.markdown("""
    <div class="navbar">
        <a class="navbar-brand" href="/">Abhiram Singuru<span>.</span></a>
        <div class="navbar-nav">
            <span style="font-family: monospace; font-size: 11px; text-transform: uppercase; color: #7c5cff; letter-spacing: 0.1em; border: 1px solid rgba(124,92,255,0.3); padding: 4px 10px; border-radius: 6px; background: rgba(124,92,255,0.05);">Uses</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Main Intro Card
    st.markdown("""
    <div class="glass-card" style="margin-top: 10px; margin-bottom: 24px;">
        <span class="section-label">§ 07 — Uses</span>
        <div class="section-title">Developer Setup & Tools</div>
        <div class="section-desc">
            A comprehensive list of hardware, editors, software utilities, and database tools I use to write, debug, and monitor code daily.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Build uses categories list HTML
    uses_categories_html = ""
    for item in uses_list:
        items_html = "".join([f"• {sub_item}<br>" for sub_item in item.get("items", [])])
        
        uses_categories_html += f"""
        <div class="glass-card" style="margin-bottom: 0;">
            <div style="font-size: 1.25rem; font-weight: 700; color: #ffffff; margin-bottom: 16px; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 8px;">{item.get("category", "")}</div>
            <div style="font-size: 14px; line-height: 1.8; color: #d1d5db;">
                {items_html}
            </div>
        </div>
        """

    st.markdown(f"""
    <div style="display: flex; flex-direction: column; gap: 24px;">
        {uses_categories_html}
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    uses()
