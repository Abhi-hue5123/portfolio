"""Tools and setup page."""

from __future__ import annotations

import streamlit as st

from utils import clean_text, inject_css, load_data, page_intro

st.set_page_config(
    page_title="Uses - Abhiram Singuru",
    page_icon="Uses",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

data = load_data()
uses = data.get("uses", [])

page_intro(
    "07 - Uses",
    "Tools & Setup",
    "Software, hardware, and services powering my daily development and database engineering workflow.",
    key="uses_intro",
)

for index, category in enumerate(uses):
    with st.container(key=f"uses_card_{index}"):
        st.subheader(category.get("category", ""))
        for item in category.get("items", []):
            st.markdown(f"- {clean_text(item)}")
