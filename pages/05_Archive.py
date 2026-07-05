"""Project archive page."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from utils import clean_text, inject_css, load_data, page_intro

st.set_page_config(
    page_title="Archive - Abhiram Singuru",
    page_icon="Archive",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

data = load_data()
archive = data.get("archive", [])

page_intro(
    "08 - Archive",
    "Full Project History",
    "A complete, chronological record of all projects, client engagements, and engineering contributions across my career.",
    key="archive_intro",
)

rows = [
    {
        "Year": entry.get("year", ""),
        "Project": clean_text(entry.get("project", "")),
        "Company": clean_text(entry.get("company", "")),
        "Stack": ", ".join(clean_text(tag) for tag in entry.get("tech_tags", [])),
    }
    for entry in archive
]

with st.container(key="archive_card"):
    st.dataframe(
        pd.DataFrame(rows),
        hide_index=True,
        width="stretch",
        column_config={
            "Year": st.column_config.NumberColumn(format="%d"),
            "Project": st.column_config.TextColumn(width="medium"),
            "Company": st.column_config.TextColumn(width="medium"),
            "Stack": st.column_config.TextColumn(width="large"),
        },
    )
