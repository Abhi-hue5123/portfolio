"""Projects page."""

from __future__ import annotations

import streamlit as st

from utils import clean_text, inject_css, load_data, page_intro, render_pills

st.set_page_config(
    page_title="Projects - Abhiram Singuru",
    page_icon="Projects",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

data = load_data()
projects = data.get("projects", [])

page_intro(
    "05 - Projects",
    "Selected Work",
    "A curated set of personal and professional projects spanning database engineering, automation pipelines, full-stack services, and AI-assisted tooling.",
    key="projects_intro",
)

for row_start in range(0, len(projects), 2):
    cols = st.columns(2, gap="medium")
    for col_index, project in enumerate(projects[row_start : row_start + 2]):
        with cols[col_index]:
            with st.container(key=f"project_card_{row_start + col_index}"):
                st.caption(project.get("category", ""))
                st.subheader(project.get("title", ""))
                st.write(clean_text(project.get("description", "")))
                render_pills(project.get("tech_tags", []), key=f"project_tags_{row_start + col_index}")
