"""Writing page."""

from __future__ import annotations

import streamlit as st

from utils import clean_text, inject_css, load_data, page_intro

st.set_page_config(
    page_title="Writing - Abhiram Singuru",
    page_icon="Writing",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

data = load_data()
writing = data.get("writing", [])

page_intro(
    "06 - Writing",
    "Articles & Tutorials",
    "Technical deep-dives, walkthroughs, and guides on Oracle databases, Unix automation, and cloud engineering.",
    key="writing_intro",
)

for index, article in enumerate(writing):
    with st.container(key=f"writing_card_{index}"):
        top = st.columns([3, 1], gap="medium")
        with top[0]:
            st.caption(article.get("category", ""))
            st.subheader(article.get("title", ""))
        with top[1]:
            st.caption(article.get("date", ""))

        st.write(clean_text(article.get("description", "")))

        link = article.get("link", "#")
        if link and link != "#":
            st.link_button("Read article", link)
        else:
            st.caption("Coming soon")
