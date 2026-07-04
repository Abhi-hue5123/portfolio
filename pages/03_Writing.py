import streamlit as st
import os
import json

# Page configs (tab title, favicon)
st.set_page_config(
    page_title="Abhiram Singuru's Writing",
    page_icon="✍️",
    layout="wide",
)

def load_portfolio_data():
    try:
        with open("portfolio_data.json", "r") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading portfolio_data.json: {e}")
        return {}

def writing():
    # Load JSON data
    data = load_portfolio_data()
    writing_list = data.get("writing", [])

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
            <span style="font-family: monospace; font-size: 11px; text-transform: uppercase; color: #7c5cff; letter-spacing: 0.1em; border: 1px solid rgba(124,92,255,0.3); padding: 4px 10px; border-radius: 6px; background: rgba(124,92,255,0.05);">Writing</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Main Intro Card
    st.markdown("""
    <div class="glass-card" style="margin-top: 10px; margin-bottom: 24px;">
        <span class="section-label">§ 06 — Writing</span>
        <div class="section-title">Articles & Technical Write-ups</div>
        <div class="section-desc">
            Sharing guides on database optimization, automation tips, and cloud architecture patterns.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Build articles list HTML
    articles_html = ""
    for item in writing_list:
        articles_html += f"""
        <div class="glass-card" style="margin-bottom: 0;">
            <div style="font-family: monospace; font-size: 11px; color: #7c5cff; margin-bottom: 8px;">{item.get("category", "")}</div>
            <h3 style="margin-top: 0; color: #ffffff; font-size: 18px; font-weight: 700; margin-bottom: 8px;">{item.get("title", "")}</h3>
            <p style="color: #9ca3af; font-size: 14px; line-height: 1.6; margin-bottom: 16px;">
                {item.get("description", "")}
            </p>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-family: monospace; font-size: 11px; color: #6b7280;">{item.get("date", "")}</span>
                <a href="{item.get("link", "#")}" style="font-family: monospace; font-size: 12px; color: #ffffff; text-decoration: none; border-bottom: 1px solid #ffffff; padding-bottom: 2px;">Read article →</a>
            </div>
        </div>
        """

    st.markdown(f"""
    <div style="display: flex; flex-direction: column; gap: 20px;">
        {articles_html}
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    writing()
