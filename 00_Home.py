"""
00_Home.py — Portfolio Landing Page
JSON-driven | Uses shared utils for CSS injection and data loading
"""
import streamlit as st
from utils import inject_css, load_data, page_header, file_to_base64, render_skill_pills

# ── Page config (ONLY set here for the entry point) ───────────────────────────
st.set_page_config(
    page_title="Abhiram Singuru — Portfolio",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Inject CSS & Spotlights ───────────────────────────────────────────────────
inject_css()
page_header("Portfolio")

# ── Load Data ─────────────────────────────────────────────────────────────────
data         = load_data()
info         = data.get("personal_info", {})
stats        = data.get("stats", [])
skills       = data.get("skills", {})
certs        = data.get("certifications", [])

# ── Asset helpers ──────────────────────────────────────────────────────────────
profile_img_b64 = file_to_base64("assets/profile_squared.png")
profile_img_src = (
    f"data:image/png;base64,{profile_img_b64}"
    if profile_img_b64
    else "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
)

pdf_b64 = file_to_base64("assets/Abhiram_Singuru_CV.pdf")

# ── Layout: two-column grid ────────────────────────────────────────────────────
left, right = st.columns([1, 2.1], gap="large")

# ── LEFT: Profile Card ─────────────────────────────────────────────────────────
with left:
    st.markdown(f"""
    <div class="profile-card">
        <div class="profile-image-container">
            <img src="{profile_img_src}" alt="{info.get('name', 'Profile Photo')}">
        </div>
        <div class="profile-name">{info.get("name", "")}</div>
        <div class="profile-title">{info.get("title", "")}</div>

        <div class="profile-socials">
            <a class="social-icon-link" href="{info.get('linkedin', '#')}" target="_blank" rel="noopener" aria-label="LinkedIn">
                <svg width="17" height="17" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/>
                </svg>
            </a>
            <a class="social-icon-link" href="{info.get('github', '#')}" target="_blank" rel="noopener" aria-label="GitHub">
                <svg width="17" height="17" fill="currentColor" viewBox="0 0 24 24">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.166 6.839 9.489.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.464-1.11-1.464-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.579.688.481C19.138 20.161 22 16.418 22 12c0-5.523-4.477-10-10-10z"/>
                </svg>
            </a>
            <a class="social-icon-link" href="mailto:{info.get('email', '')}" aria-label="Email">
                <svg width="17" height="17" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z"/>
                </svg>
            </a>
        </div>

        <div class="profile-info-row">
            <div class="profile-info-item">
                <div class="profile-info-label">Based in</div>
                <div class="profile-info-value">{info.get("location", "")}</div>
            </div>
            <div class="profile-info-item">
                <div class="profile-info-label">Timezone</div>
                <div class="profile-info-value">{info.get("timezone", "")}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── RIGHT: Hero + Content ──────────────────────────────────────────────────────
with right:
    # ── Status Badge + Hero ──
    st.markdown(f"""
    <div class="status-badge">{info.get("status_badge", "Open to opportunities")}</div>
    <h1 class="hero-title">{info.get("hero_title", info.get("name", ""))}</h1>
    <p class="hero-subtitle">{info.get("hero_subtitle", "")}</p>
    """, unsafe_allow_html=True)

    # ── CTA Buttons ──
    pdf_btn = ""
    if pdf_b64:
        pdf_btn = f"""
        <a class="btn-secondary" href="data:application/pdf;base64,{pdf_b64}" download="Abhiram_Singuru_CV.pdf">
            ↓ Download CV
        </a>"""

    st.markdown(f"""
    <div class="btn-container">
        <a class="btn-primary" href="mailto:{info.get('email', '')}">
            Get in touch
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>
            </svg>
        </a>
        {pdf_btn}
    </div>
    """, unsafe_allow_html=True)

    # ── About Me ──
    bullets_html = "".join(
        f'<div class="about-bullet">{b}</div>'
        for b in info.get("about_bullets", [])
    )
    st.markdown(f"""
    <div class="glass-card">
        <span class="section-label">{info.get("about_label", "§ 01 — About")}</span>
        <div class="section-title">{info.get("about_title", "About Me")}</div>
        <div class="section-desc">{info.get("about_desc", "")}</div>
        <div>{bullets_html}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Tech Stack ──
    primary_html   = render_skill_pills(skills.get("primary", []),   "skill-pill-primary")
    secondary_html = render_skill_pills(skills.get("secondary", []), "skill-pill-secondary")
    st.markdown(f"""
    <div class="glass-card">
        <span class="section-label">§ 02 — Stack</span>
        <div class="section-title">Technical Expertise</div>
        <div class="skill-group-title">Primary Focus</div>
        <div>{primary_html}</div>
        <div class="skill-group-title">Frameworks &amp; Tools</div>
        <div>{secondary_html}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Certifications ──
    certs_html = "".join(f"""
    <div class="cert-row">
        <div class="cert-title">{c.get("title", "")}</div>
        <div class="cert-dates">{c.get("dates", "")}</div>
    </div>
    """ for c in certs)
    st.markdown(f"""
    <div class="glass-card">
        <span class="section-label">§ 03 — Credentials</span>
        <div class="section-title">Certifications</div>
        <div>{certs_html}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Stats Grid ──
    stats_html = "".join(f"""
    <div class="stats-item">
        <div class="stats-number">{s.get("number", "")}</div>
        <div class="stats-label">{s.get("label", "")}</div>
    </div>
    """ for s in stats)
    st.markdown(f"""
    <div class="stats-grid">{stats_html}</div>
    """, unsafe_allow_html=True)