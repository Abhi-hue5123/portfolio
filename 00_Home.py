"""App entry point: global config, top navigation, and the shared identity strip."""

from __future__ import annotations

import streamlit as st

from utils import inject_css, load_data, load_resume_bytes, render_top_identity

st.set_page_config(
    page_title="Abhiram Singuru - Portfolio",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_css()

data = load_data()
info = data.get("personal_info", {})
resume_bytes = load_resume_bytes()

render_top_identity(info, resume_bytes)

pages = [
    st.Page("views/00_Home.py", title="Home", icon="🏠", default=True),
    st.Page("views/01_Work_Experience.py", title="Experience", icon="💼"),
    st.Page("views/02_Projects.py", title="Projects", icon="🧩"),
    st.Page("views/03_Writing.py", title="Writing", icon="✍️"),
    st.Page("views/04_Uses.py", title="Uses", icon="🛠️"),
    st.Page("views/05_Archive.py", title="Archive", icon="🗂️"),
    st.Page("views/06_Contact.py", title="Contact", icon="✉️"),
]

pg = st.navigation(pages, position="top")
pg.run()
