"""Shared helpers for the Streamlit portfolio."""

from __future__ import annotations

import json
import re
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent
DATA_FILE = ROOT_DIR / "portfolio_data.json"
CSS_FILE = ROOT_DIR / "styles" / "main.css"
PROFILE_IMAGE = ROOT_DIR / "assets" / "profile_squared.png"
RESUME_FILE = ROOT_DIR / "assets" / "Abhiram_Singuru_CV.pdf"


@st.cache_data(show_spinner=False)
def load_data() -> dict:
    """Load portfolio data once per session."""
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except OSError as exc:
        st.error(f"Could not load portfolio_data.json: {exc}")
    except json.JSONDecodeError as exc:
        st.error(f"portfolio_data.json is not valid JSON: {exc}")
    return {}


@st.cache_data(show_spinner=False)
def load_css() -> str:
    """Load the production stylesheet."""
    try:
        return CSS_FILE.read_text(encoding="utf-8")
    except OSError as exc:
        st.error(f"Could not load styles/main.css: {exc}")
        return ""


@st.cache_data(show_spinner=False)
def load_resume_bytes() -> bytes | None:
    """Load the resume PDF for Streamlit's native download button."""
    try:
        return RESUME_FILE.read_bytes()
    except OSError:
        return None


def inject_css() -> None:
    """Inject global CSS through Streamlit's HTML API."""
    css = load_css()
    if css:
        st.html(f"<style>{css}</style>")


def page_intro(label: str, title: str, description: str, key: str = "page_intro") -> None:
    """Render a consistent page introduction with native Streamlit elements."""
    with st.container(key=key):
        st.caption(label)
        st.title(title)
        st.write(description)


def clean_text(value: str) -> str:
    """Remove legacy HTML tags from data before displaying as text/markdown."""
    value = re.sub(r"</?b>", "**", value)
    return re.sub(r"<[^>]+>", "", value)


def render_pills(items: list[str], key: str, variant: str = "secondary") -> None:
    """Render compact Streamlit badges for skills and tech tags."""
    if not items:
        return

    with st.container(key=key):
        max_cols = min(max(1, len(items)), 4)
        cols = st.columns(max_cols, gap="small")
        for index, item in enumerate(items):
            with cols[index % max_cols]:
                badge_type = "blue" if variant == "primary" else "gray"
                st.badge(clean_text(item), color=badge_type)


def render_section_card(label: str, title: str, description: str, key: str):
    """Open a styled container and render the common section header."""
    card = st.container(key=key)
    with card:
        st.caption(label)
        st.subheader(title)
        st.write(description)
    return card
