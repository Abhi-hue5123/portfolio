import streamlit as st
import base64
import os
import json

# Page configs (tab title, favicon)
st.set_page_config(
    page_title="Abhiram Singuru's Portfolio",
    page_icon="🧑‍💻",
    layout="wide",
)

def load_portfolio_data():
    try:
        with open("portfolio_data.json", "r") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading portfolio_data.json: {e}")
        return {}

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def home():
    # Load JSON data
    data = load_portfolio_data()
    info = data.get("personal_info", {})
    stats = data.get("stats", [])
    skills = data.get("skills", {})
    certifications = data.get("certifications", [])

    # Injects the glowing spotlights into the background
    st.markdown('<div class="glow-spotlight-1"></div><div class="glow-spotlight-2"></div>', unsafe_allow_html=True)

    # CSS styles file
    if os.path.exists("styles/main.css"):
        with open("styles/main.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image base64
    profile_img_base64 = ""
    if os.path.exists("assets/profile_squared.png"):
        profile_img_base64 = "data:image/png;base64," + get_base64_of_bin_file("assets/profile_squared.png")
    else:
        profile_img_base64 = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"

    # PDF CV base64
    pdf_base64 = ""
    if os.path.exists("assets/Abhiram_Singuru_CV.pdf"):
        pdf_base64 = get_base64_of_bin_file("assets/Abhiram_Singuru_CV.pdf")

    # Navbar Logotype Mockup
    st.markdown(f"""
    <div class="navbar">
        <a class="navbar-brand" href="#">{info.get("name", "Portfolio")}<span>.</span></a>
        <div class="navbar-nav">
            <span style="font-family: monospace; font-size: 11px; text-transform: uppercase; color: #7c5cff; letter-spacing: 0.1em; border: 1px solid rgba(124,92,255,0.3); padding: 4px 10px; border-radius: 6px; background: rgba(124,92,255,0.05);">Portfolio</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Grid layout: Left Column (Profile card) and Right Column (Content)
    col1, col2 = st.columns([1, 2.2])

    with col1:
        st.markdown(f"""
        <div class="profile-card">
            <div class="profile-image-container">
                <img src="{profile_img_base64}" alt="{info.get("name", "")}">
            </div>
            <div class="profile-name">{info.get("name", "")}</div>
            <div class="profile-title">{info.get("title", "")}</div>
            
            <div class="profile-socials">
                <a class="social-icon-link" href="{info.get("linkedin", "#")}" target="_blank" aria-label="LinkedIn">
                    <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/>
                    </svg>
                </a>
                <a class="social-icon-link" href="{info.get("github", "#")}" target="_blank" aria-label="GitHub">
                    <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.166 6.839 9.489.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.464-1.11-1.464-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.579.688.481C19.138 20.161 22 16.418 22 12c0-5.523-4.477-10-10-10z"/>
                    </svg>
                </a>
                <a class="social-icon-link" href="mailto:{info.get("email", "")}" aria-label="Email">
                    <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z"/>
                    </svg>
                </a>
            </div>
            
            <div class="profile-info-row">
                <div class="profile-info-item">
                    <div class="profile-info-label">Based in</div>
                    <div class="profile-info-value">{info.get("location", "")}</div>
                </div>
                <div class="profile-info-item" style="text-align: right;">
                    <div class="profile-info-label">Timezone</div>
                    <div class="profile-info-value">{info.get("timezone", "")}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Hero Intro Section
        st.markdown(f"""
        <div class="status-badge">{info.get("status_badge", "")}</div>
        <h1 class="hero-title">{info.get("hero_title", "")}</h1>
        <p class="hero-subtitle">
            {info.get("hero_subtitle", "")}
        </p>
        """, unsafe_allow_html=True)

        # Action Buttons
        btn_html = f"""
        <div class="btn-container">
            <a class="btn-primary" href="mailto:{info.get("email", "")}">
                Get in touch
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                    <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
            </a>
        """
        if pdf_base64:
            btn_html += f"""
            <a class="btn-secondary" href="data:application/pdf;base64,{pdf_base64}" download="Abhiram_Singuru_CV.pdf">
                Download CV
            </a>
            """
        btn_html += "</div>"
        st.markdown(btn_html, unsafe_allow_html=True)

        # About Me Section
        bullets_html = "".join([f"• {bullet}<br>" for bullet in info.get("about_bullets", [])])
        st.markdown(f"""
        <div class="glass-card">
            <span class="section-label">{info.get("about_label", "§ 01 — About")}</span>
            <div class="section-title">{info.get("about_title", "")}</div>
            <div class="section-desc">
                {info.get("about_desc", "")}
            </div>
            <div style="color: rgba(255, 255, 255, 0.85); font-size: 14px; line-height: 1.6;">
                {bullets_html}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Skills & Tech Stack Section
        primary_skills_html = "".join([f'<span class="skill-pill-primary">{skill}</span>' for skill in skills.get("primary", [])])
        secondary_skills_html = "".join([f'<span class="skill-pill-secondary">{skill}</span>' for skill in skills.get("secondary", [])])
        st.markdown(f"""
        <div class="glass-card">
            <span class="section-label">§ 02 — Stack</span>
            <div class="section-title">Technical Expertise</div>
            
            <div class="skill-group-title">Primary Focus</div>
            <div>
                {primary_skills_html}
            </div>
            
            <div class="skill-group-title">Frameworks & Tools</div>
            <div>
                {secondary_skills_html}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Certifications Section
        certifications_html = ""
        for i, cert in enumerate(certifications):
            border_style = "border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 8px; margin-bottom: 12px;" if i < len(certifications) - 1 else ""
            certifications_html += f"""
            <div style="{border_style} display: flex; justify-content: space-between; align-items: center;">
                <div><b>{cert.get("title", "")}</b></div>
                <div style="color: #7c5cff; font-family: monospace; white-space: nowrap; margin-left: 10px;">{cert.get("dates", "")}</div>
            </div>
            """
        st.markdown(f"""
        <div class="glass-card">
            <span class="section-label">§ 03 — Credentials</span>
            <div class="section-title">Certifications</div>
            <div style="font-size: 14px; line-height: 1.6; color: #d1d5db;">
                {certifications_html}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Statistics Grid
        stats_html = ""
        for stat in stats:
            stats_html += f"""
            <div class="stats-item">
                <div class="stats-number">{stat.get("number", "")}</div>
                <div class="stats-label">{stat.get("label", "")}</div>
            </div>
            """
        st.markdown(f"""
        <div class="stats-grid">
            {stats_html}
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    home()