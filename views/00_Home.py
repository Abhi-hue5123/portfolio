"""Portfolio landing page."""

from __future__ import annotations

import streamlit as st

from utils import (
    PROFILE_IMAGE,
    clean_text,
    load_data,
    load_resume_bytes,
    render_education,
    render_marquee,
    render_pills,
    render_social_row,
    render_testimonials,
)

data = load_data()
info = data.get("personal_info", {})
stats = data.get("stats", [])
skills = data.get("skills", {})
certifications = data.get("certifications", [])
experience_list = data.get("experience", [])
education_list = data.get("education", [])
testimonials = data.get("testimonials", [])
projects = data.get("projects", [])
resume_bytes = load_resume_bytes()

hero_left, hero_right = st.columns([1.8, 1], gap="large")

with hero_left:
    with st.container(key="hero_copy"):
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
                width="stretch",
            )

    render_social_row(info, key="hero_social_row")

    if stats:
        stat_cols = st.columns(len(stats), gap="small")
        for index, stat in enumerate(stats):
            with stat_cols[index]:
                st.metric(stat.get("label", ""), stat.get("number", ""))

with hero_right:
    if PROFILE_IMAGE.exists():
        with st.container(key="hero_portrait"):
            st.image(str(PROFILE_IMAGE), width="stretch")

st.write("---")

tabs = st.tabs(
    [
        "About",
        "Stack",
        "Credentials",
        "Education",
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
        render_marquee(skills.get("primary", []), key="primary_skills_marquee")
        if skills.get("secondary"):
            st.caption("Frameworks & tools")
            render_marquee(skills.get("secondary", []), key="secondary_skills_marquee")

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
    with st.container(key="education_intro"):
        st.caption("04 - Education")
        st.subheader("Academic Background")
    render_education(education_list, key="home_education")

with tabs[4]:
    with st.container(key="experience_intro"):
        st.caption("05 - Experience")
        st.subheader("Professional Experience")

    for index, item in enumerate(experience_list):
        with st.expander(f"{item.get('title', '')} · {item.get('company', '')}", expanded=index == 0):
            st.caption(item.get("date", ""))
            for bullet in item.get("bullet_points", []):
                st.markdown(f"- {clean_text(bullet)}")
            render_pills(item.get("tech_tags", []), key=f"experience_tags_{index}", variant="primary")

st.write("---")

with st.container(key="featured_projects_intro"):
    top = st.columns([3, 1], gap="medium")
    with top[0]:
        st.caption("06 - Selected Work")
        st.subheader("Featured Projects")
    with top[1]:
        st.page_link("views/02_Projects.py", label="View all projects →")

featured = projects[:2]
if featured:
    feature_cols = st.columns(len(featured), gap="medium")
    for index, project in enumerate(featured):
        with feature_cols[index]:
            with st.container(key=f"featured_project_card_{index}"):
                st.caption(project.get("category", ""))
                st.subheader(project.get("title", ""))
                st.write(clean_text(project.get("description", "")))
                render_pills(project.get("tech_tags", []), key=f"featured_project_tags_{index}")

st.write("---")

with st.container(key="testimonials_intro"):
    st.caption("07 - Recommendations")
    st.subheader("What People Say")
render_testimonials(testimonials, key="home_testimonials")

st.write("---")

with st.container(key="cta_banner"):
    cta_cols = st.columns([2, 1], gap="large")
    with cta_cols[0]:
        st.subheader("Let's build something reliable together.")
        st.write("Open to full-time roles and consulting work in data engineering, ETL, and cloud pipelines.")
    with cta_cols[1]:
        st.page_link("views/06_Contact.py", label="Get in touch →", width="stretch")
