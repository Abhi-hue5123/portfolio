"""Shared helpers for the Streamlit portfolio."""

from __future__ import annotations

import base64
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


_ICON_COLOR = "#ededee"

_SOCIAL_ICONS = {
    "email": (
        '<svg viewBox="0 0 24 24" width="18" height="18" style="display:block;fill:none;'
        f'stroke:{_ICON_COLOR};stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round">'
        '<rect x="2.5" y="4.5" width="19" height="15" rx="2.2"/><path d="M3 6.5l9 6.2 9-6.2"/></svg>'
    ),
    "linkedin": (
        '<svg viewBox="0 0 24 24" width="18" height="18" style="display:block;'
        f'fill:{_ICON_COLOR}">'
        '<path d="M4.98 3.5a2.5 2.5 0 11-.02 5 2.5 2.5 0 01.02-5zM3 9h4v12H3zM9 9h3.8v1.64h.05c.53-.98 '
        "1.83-2.02 3.77-2.02 4.03 0 4.78 2.55 4.78 5.86V21h-4v-5.6c0-1.34-.02-3.06-1.87-3.06-1.87 "
        '0-2.16 1.44-2.16 2.96V21H9z"/></svg>'
    ),
    "github": (
        '<svg viewBox="0 0 24 24" width="18" height="18" style="display:block;'
        f'fill:{_ICON_COLOR}">'
        "<path d=\"M12 2C6.48 2 2 6.58 2 12.2c0 4.5 2.87 8.32 6.84 9.67.5.1.68-.22.68-.49 "
        "0-.24-.01-1.03-.01-1.87-2.78.62-3.37-1.21-3.37-1.21-.46-1.19-1.11-1.51-1.11-1.51-.9-.63.07-.62.07-.62 "
        "1 .07 1.53 1.05 1.53 1.05.89 1.55 2.34 1.1 2.91.84.09-.66.35-1.1.63-1.36-2.22-.26-4.56-1.14-4.56-5.07 "
        "0-1.12.39-2.03 1.03-2.75-.1-.26-.45-1.32.1-2.75 0 0 .84-.27 2.75 1.05a9.3 9.3 0 015 0c1.91-1.32 "
        "2.75-1.05 2.75-1.05.55 1.43.2 2.49.1 2.75.64.72 1.03 1.63 1.03 2.75 0 3.94-2.35 4.8-4.58 5.06.36.32 "
        "0.68.94.68 1.9 0 1.37-.01 2.47-.01 2.81 0 .27.18.6.69.49A10.02 10.02 0 0022 12.2C22 6.58 17.52 2 "
        '12 2z"/></svg>'
    ),
}


def _svg_data_uri(svg: str) -> str:
    """Encode raw SVG markup as a base64 data URI.

    st.html() runs its markup through DOMPurify with USE_PROFILES={"html": True},
    which silently strips every <svg> element (no SVG profile allowed). Embedding
    the icon as an <img src="data:image/svg+xml;base64,..."> sidesteps that
    entirely, since the SVG never exists as DOM nodes for the sanitizer to see.
    """
    encoded = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded}"


def _social_link_html(icon_key: str, href: str, label: str) -> str:
    icon_svg = _SOCIAL_ICONS.get(icon_key, "")
    data_uri = _svg_data_uri(icon_svg)
    return (
        f'<a class="pf-social-btn" href="{href}" target="_blank" rel="noopener noreferrer" '
        f'title="{label}" aria-label="{label}">'
        f'<img src="{data_uri}" width="18" height="18" alt="{label}" style="display:block"/></a>'
    )


def render_social_row(info: dict, key: str = "social_row") -> None:
    """Render a compact row of icon-only social links."""
    links_html = []
    if info.get("email"):
        links_html.append(_social_link_html("email", f"mailto:{info['email']}", "Email"))
    if info.get("linkedin"):
        links_html.append(_social_link_html("linkedin", info["linkedin"], "LinkedIn"))
    if info.get("github"):
        links_html.append(_social_link_html("github", info["github"], "GitHub"))
    if not links_html:
        return
    with st.container(key=key):
        st.html(f'<div class="pf-social-row">{"".join(links_html)}</div>')


def render_top_identity(info: dict, resume_bytes: bytes | None) -> None:
    """Render a slim identity strip beneath the top nav, shown on every page."""
    with st.container(key="identity_bar"):
        left, right = st.columns([2.2, 1], gap="medium", vertical_alignment="center")

        with left:
            inner = st.columns([0.09, 0.91], gap="small", vertical_alignment="center")
            with inner[0]:
                if PROFILE_IMAGE.exists():
                    st.image(str(PROFILE_IMAGE), width="stretch")
            with inner[1]:
                name_bits = st.columns([1, 1], gap="small", vertical_alignment="center")
                with name_bits[0]:
                    st.markdown(f'<div class="pf-identity-name">{info.get("name", "")}</div>', unsafe_allow_html=True)
                badge = info.get("status_badge")
                if badge:
                    with name_bits[1]:
                        st.badge(badge, color="green")
                st.caption(info.get("title", ""))

        with right:
            controls = st.columns([1.2, 1], gap="small", vertical_alignment="center")
            with controls[0]:
                render_social_row(info, key="identity_social_row")
            with controls[1]:
                if resume_bytes:
                    st.download_button(
                        "Download CV",
                        data=resume_bytes,
                        file_name="Abhiram_Singuru_CV.pdf",
                        mime="application/pdf",
                        width="stretch",
                        key="identity_cv_download",
                    )


def render_marquee(items: list[str], key: str) -> None:
    """Render an infinitely scrolling row of tech chips."""
    if not items:
        return
    chips = "".join(f'<span class="pf-marquee-chip">{clean_text(item)}</span>' for item in items)
    with st.container(key=key):
        st.html(f'<div class="pf-marquee"><div class="pf-marquee-track">{chips}{chips}</div></div>')


def render_education(education: list[dict], key: str = "education") -> None:
    """Render an education timeline section."""
    if not education:
        return
    with st.container(key=key):
        for index, entry in enumerate(education):
            with st.container(key=f"{key}_item_{index}"):
                top = st.columns([3, 1], gap="medium")
                with top[0]:
                    st.markdown(f"**{clean_text(entry.get('degree', ''))}**")
                    st.write(clean_text(entry.get("institution", "")))
                with top[1]:
                    st.caption(entry.get("dates", ""))
                if entry.get("description"):
                    st.caption(clean_text(entry["description"]))


def render_testimonials(testimonials: list[dict], key: str = "testimonials") -> None:
    """Render a grid of testimonial/recommendation cards."""
    if not testimonials:
        return
    with st.container(key=key):
        cols = st.columns(min(len(testimonials), 2), gap="medium")
        for index, entry in enumerate(testimonials):
            with cols[index % len(cols)]:
                with st.container(key=f"{key}_card_{index}"):
                    st.markdown(f'<div class="pf-quote-mark">&ldquo;</div>', unsafe_allow_html=True)
                    st.write(clean_text(entry.get("quote", "")))
                    who = entry.get("name", "")
                    role_bits = [bit for bit in (entry.get("title"), entry.get("company")) if bit]
                    if who:
                        st.markdown(f"**{who}**")
                    if role_bits:
                        st.caption(" · ".join(role_bits))
