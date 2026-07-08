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
experience_list = data.get("experience", [])
resume_bytes = load_resume_bytes()

hero_left, hero_right = st.columns([1.8, 1], gap="large")

with hero_left:
    st.caption(info.get("status_badge", "Available for opportunities"))
    st.title(info.get("hero_title", info.get("name", "")))
    st.write(info.get("hero_subtitle", ""))

    call_to_action = st.columns([1, 1], gap="small")
    with call_to_action[0]:
        st.link_button("Get in touch", f"mailto:{info.get('email', '')}", type="primary")
    with call_to_action[1]:
        if resume_bytes:
            st.download_button(
                "Download CV",
                data=resume_bytes,
                file_name="Abhiram_Singuru_CV.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

    if stats:
        stat_cols = st.columns(len(stats), gap="small")
        for index, stat in enumerate(stats):
            with stat_cols[index]:
                st.metric(stat.get("label", ""), stat.get("number", ""))

with hero_right:
    if PROFILE_IMAGE.exists():
        st.image(str(PROFILE_IMAGE), use_column_width="always")

st.write("---")

tabs = st.tabs(
    [
        "About",
        "Stack",
        "Credentials",
        "Experience",
    ]
)

with tabs[0]:
    with st.container(key="about_card"):
        st.caption(info.get("about_label", "01 - About"))
        st.subheader(info.get("about_title", "About Me"))
        st.write(info.get("about_desc", ""))
        for bullet in info.get("about_bullets", []):
            st.markdown(f"- {clean_text(bullet)}")

with tabs[1]:
    with st.container(key="skills_card"):
        st.caption("02 - Stack")
        st.subheader("Technical Expertise")
        st.caption("Primary focus")
        render_pills(skills.get("primary", []), key="primary_skills", variant="primary")
        if skills.get("secondary"):
            st.caption("Frameworks & tools")
            render_pills(skills.get("secondary", []), key="secondary_skills")

with tabs[2]:
    with st.container(key="certifications_card"):
        st.caption("03 - Credentials")
        st.subheader("Certifications")
        for certification in certifications:
            cert_cols = st.columns([3, 1], gap="medium")
            with cert_cols[0]:
                st.write(certification.get("title", ""))
            with cert_cols[1]:
                st.caption(certification.get("dates", ""))

with tabs[3]:
    with st.container(key="experience_intro"):
        st.caption("04 - Experience")
        st.subheader("Professional Experience")

    for index, item in enumerate(experience_list):
        with st.expander(f"{item.get('title', '')} · {item.get('company', '')}", expanded=index == 0):
            st.caption(item.get("date", ""))
            for bullet in item.get("bullet_points", []):
                st.markdown(f"- {clean_text(bullet)}")
            render_pills(item.get("tech_tags", []), key=f"experience_tags_{index}", variant="primary")
