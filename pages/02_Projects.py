import streamlit as st
import os
import json

# Page configs (tab title, favicon)
st.set_page_config(
    page_title="Abhiram Singuru's Projects",
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

def projects():
    # Load JSON data
    data = load_portfolio_data()
    project_list = data.get("projects", [])

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
            <span style="font-family: monospace; font-size: 11px; text-transform: uppercase; color: #7c5cff; letter-spacing: 0.1em; border: 1px solid rgba(124,92,255,0.3); padding: 4px 10px; border-radius: 6px; background: rgba(124,92,255,0.05);">Projects</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Main Intro Card
    st.markdown("""
    <div class="glass-card" style="margin-top: 10px; margin-bottom: 24px;">
        <span class="section-label">§ 05 — Projects</span>
        <div class="section-title">Selected Technical Projects</div>
        <div class="section-desc">
            A showcase of database utilities, automation scripts, and cloud tooling built to solve operational bottlenecks and improve query execution speeds.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Build projects grid HTML
    projects_grid_html = ""
    for item in project_list:
        tech_tags_html = "".join([f'<span class="tech-badge">{tag}</span>' for tag in item.get("tech_tags", [])])
        
        projects_grid_html += f"""
        <div class="glass-card" style="margin-bottom: 0;">
            <div style="display: flex; justify-content: space-between; align-items: start;">
                <h3 style="margin-top: 0; color: #ffffff; font-size: 18px; font-weight: 700;">{item.get("title", "")}</h3>
                <span style="font-family: monospace; font-size: 11px; color: #7c5cff; border: 1px solid rgba(124,92,255,0.2); padding: 2px 8px; border-radius: 4px; background: rgba(124,92,255,0.03);">{item.get("category", "")}</span>
            </div>
            <p style="color: #9ca3af; font-size: 14px; line-height: 1.6; margin-top: 12px; margin-bottom: 16px;">
                {item.get("description", "")}
            </p>
            <div style="margin-top: auto;">
                {tech_tags_html}
            </div>
        </div>
        """

    st.markdown(f"""
    <div style="display: grid; grid-template-columns: 1fr; gap: 24px; margin-top: 16px;">
        {projects_grid_html}
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    projects()
