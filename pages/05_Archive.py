import streamlit as st
import os
import json

# Page configs (tab title, favicon)
st.set_page_config(
    page_title="Abhiram Singuru's Archive",
    page_icon="🗄️",
    layout="wide",
)

def load_portfolio_data():
    try:
        with open("portfolio_data.json", "r") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading portfolio_data.json: {e}")
        return {}

def archive():
    # Load JSON data
    data = load_portfolio_data()
    archive_list = data.get("archive", [])

    # Injects the glowing spotlights into the background
    st.markdown('<div class="glow-spotlight-1"></div><div class="glow-spotlight-2"></div>', unsafe_allow_html=True)

    # CSS styles file
    if os.path.exists("styles/main.css"):
        with open("styles/main.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Local styles for the Archive table
    st.markdown("""
    <style>
    .archive-table-wrapper {
        width: 100%;
        overflow-x: auto;
    }
    .archive-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 16px;
    }
    .archive-table th {
        font-family: monospace;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #9ca3af;
        text-align: left;
        padding: 12px 16px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }
    .archive-table td {
        padding: 16px;
        font-size: 14px;
        color: #d1d5db;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        vertical-align: middle;
    }
    .archive-table tr:hover td {
        color: #ffffff;
        background-color: rgba(255, 255, 255, 0.01);
    }
    .archive-year {
        font-family: monospace;
        color: #7c5cff;
        font-weight: 600;
    }
    .archive-project-name {
        font-weight: 600;
        color: #ffffff;
    }
    .archive-tech-tag {
        display: inline-block;
        font-family: monospace;
        font-size: 10px;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 4px;
        padding: 2px 6px;
        margin-right: 4px;
        margin-bottom: 4px;
        color: #9ca3af;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header / Navigation logotype mockup
    st.markdown("""
    <div class="navbar">
        <a class="navbar-brand" href="/">Abhiram Singuru<span>.</span></a>
        <div class="navbar-nav">
            <span style="font-family: monospace; font-size: 11px; text-transform: uppercase; color: #7c5cff; letter-spacing: 0.1em; border: 1px solid rgba(124,92,255,0.3); padding: 4px 10px; border-radius: 6px; background: rgba(124,92,255,0.05);">Archive</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Build archive rows
    archive_rows_html = ""
    for item in archive_list:
        tech_tags_html = "".join([f'<span class="archive-tech-tag">{tag}</span>' for tag in item.get("tech_tags", [])])
        
        archive_rows_html += f"""
        <tr>
            <td class="archive-year">{item.get("year", "")}</td>
            <td class="archive-project-name">{item.get("project", "")}</td>
            <td>{item.get("company", "")}</td>
            <td>
                {tech_tags_html}
            </td>
        </tr>
        """

    # Main Intro Card containing table
    st.markdown(f"""
    <div class="glass-card" style="margin-top: 10px; margin-bottom: 24px;">
        <span class="section-label">§ 08 — Archive</span>
        <div class="section-title">All Project Archive</div>
        <div class="section-desc">
            A comprehensive list of every client integration, tool creation, script development, and database project I have worked on.
        </div>
        
        <div class="archive-table-wrapper">
            <table class="archive-table">
                <thead>
                    <tr>
                        <th style="width: 10%;">Year</th>
                        <th style="width: 35%;">Project Name</th>
                        <th style="width: 20%;">Company / Client</th>
                        <th style="width: 35%;">Built With</th>
                    </tr>
                </thead>
                <tbody>
                    {archive_rows_html}
                </tbody>
            </table>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    archive()
