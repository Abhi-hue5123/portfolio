"""Work experience page."""

from __future__ import annotations

import streamlit as st

from utils import clean_text, inject_css, load_data, page_intro, render_pills

st.set_page_config(
    page_title="Work Experience - Abhiram Singuru",
    page_icon="Work",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

data = load_data()
experience_list = data.get("experience", [])

page_intro(
    "04 - Experience",
    "Professional Experience",
    "A chronological timeline of my engineering roles, project contributions, and database optimizations at Cognizant Technology Solutions.",
    key="experience_intro",
)

for index, item in enumerate(experience_list):
    with st.container(key=f"experience_card_{index}"):
        st.caption(item.get("date", ""))
        st.subheader(item.get("title", ""))
        st.write(item.get("company", ""))

        for bullet in item.get("bullet_points", []):
            st.markdown(f"- {clean_text(bullet)}")

        render_pills(item.get("tech_tags", []), key=f"experience_tags_{index}", variant="primary")
