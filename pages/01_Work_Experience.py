import streamlit as st
import os
import json

# Page configs (tab title, favicon)
st.set_page_config(
    page_title="Abhiram Singuru's Experience",
    page_icon="💼",
    layout="wide",
)

def load_portfolio_data():
    try:
        with open("portfolio_data.json", "r") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading portfolio_data.json: {e}")
        return {}

def experience():
    # Load JSON data
    data = load_portfolio_data()
    experience_list = data.get("experience", [])

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
            <span style="font-family: monospace; font-size: 11px; text-transform: uppercase; color: #7c5cff; letter-spacing: 0.1em; border: 1px solid rgba(124,92,255,0.3); padding: 4px 10px; border-radius: 6px; background: rgba(124,92,255,0.05);">Experience</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Build timeline HTML
    timeline_items_html = ""
    for item in experience_list:
        bullets_html = "".join([f"<li>{bullet}</li>" for bullet in item.get("bullet_points", [])])
        tech_tags_html = "".join([f'<span class="tech-badge">{tag}</span>' for tag in item.get("tech_tags", [])])
        
        timeline_items_html += f"""
        <div class="timeline-item">
            <div class="timeline-date">{item.get("date", "")}</div>
            <div class="timeline-title">{item.get("title", "")}</div>
            <div class="timeline-company">{item.get("company", "")}</div>
            <div class="timeline-content">
                <ul>
                    {bullets_html}
                </ul>
                <div style="margin-top: 12px;">
                    {tech_tags_html}
                </div>
            </div>
        </div>
        """

    # Render main card with timeline container
    st.markdown(f"""
    <div class="glass-card" style="margin-top: 10px;">
        <span class="section-label">§ 04 — Experience</span>
        <div class="section-title">Professional Experience</div>
        <div class="section-desc">
            A chronological timeline of my engineering roles, key project contributions, and database optimizations at Cognizant Technology Solutions.
        </div>
        
        <div class="timeline-container">
            {timeline_items_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    experience()