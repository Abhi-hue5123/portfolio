"""Portfolio landing page."""

from __future__ import annotations

import streamlit as st

from utils import (
    PROFILE_IMAGE,
    clean_text,
    inject_css,
    load_data,
    load_resume_bytes,
    render_pills,
)

st.set_page_config(
    page_title="Abhiram Singuru - Portfolio",
    page_icon="AS",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

data = load_data()
info = data.get("personal_info", {})
stats = data.get("stats", [])
skills = data.get("skills", {})
certifications = data.get("certifications", [])
resume_bytes = load_resume_bytes()

left, right = st.columns([0.95, 2.05], gap="large", vertical_alignment="top")

with left:
    with st.container(key="profile_card"):
        if PROFILE_IMAGE.exists():
            st.image(str(PROFILE_IMAGE), width="stretch")

        st.subheader(info.get("name", "Abhiram Singuru"))
        st.write(info.get("title", "Oracle PL/SQL Developer"))

        social_cols = st.columns(3, gap="small")
        with social_cols[0]:
            st.link_button("LinkedIn", info.get("linkedin", "#"), width="stretch")
        with social_cols[1]:
            st.link_button("GitHub", info.get("github", "#"), width="stretch")
        with social_cols[2]:
            st.link_button("Email", f"mailto:{info.get('email', '')}", width="stretch")

        meta_cols = st.columns(2, gap="small")
        with meta_cols[0]:
            st.caption("Based in")
            st.write(info.get("location", ""))
        with meta_cols[1]:
            st.caption("Timezone")
            st.write(info.get("timezone", ""))

with right:
    st.caption(info.get("status_badge", "Available for opportunities"))
    st.title(info.get("hero_title", info.get("name", "")))
    st.write(info.get("hero_subtitle", ""))

    cta_cols = st.columns([1, 1, 3], gap="small")
    with cta_cols[0]:
        st.link_button("Get in touch", f"mailto:{info.get('email', '')}", type="primary")
    with cta_cols[1]:
        if resume_bytes:
            st.download_button(
                "Download CV",
                data=resume_bytes,
                file_name="Abhiram_Singuru_CV.pdf",
                mime="application/pdf",
            )

    with st.container(key="about_card"):
        st.caption(info.get("about_label", "01 - About"))
        st.subheader(info.get("about_title", "About Me"))
        st.write(info.get("about_desc", ""))
        for bullet in info.get("about_bullets", []):
            st.markdown(f"- {clean_text(bullet)}")

    with st.container(key="skills_card"):
        st.caption("02 - Stack")
        st.subheader("Technical Expertise")
        st.caption("Primary focus")
        render_pills(skills.get("primary", []), key="primary_skills", variant="primary")
        st.caption("Frameworks & tools")
        render_pills(skills.get("secondary", []), key="secondary_skills")

    with st.container(key="certifications_card"):
        st.caption("03 - Credentials")
        st.subheader("Certifications")
        for certification in certifications:
            cert_cols = st.columns([3, 1], gap="medium")
            with cert_cols[0]:
                st.write(certification.get("title", ""))
            with cert_cols[1]:
                st.caption(certification.get("dates", ""))

    if stats:
        stat_cols = st.columns(len(stats), gap="small")
        for index, stat in enumerate(stats):
            with stat_cols[index]:
                st.metric(stat.get("label", ""), stat.get("number", ""))
