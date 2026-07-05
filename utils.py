"""
utils.py — Shared utility functions for all portfolio pages.
Handles JSON loading (cached), CSS injection, and common HTML helpers.
"""
import os
import json
import base64
import streamlit as st

# ─── Resolve the project root reliably (works locally AND on Streamlit Cloud) ─
_HERE = os.path.dirname(os.path.abspath(__file__))


def _path(*parts: str) -> str:
    """Return absolute path relative to the project root."""
    return os.path.join(_HERE, *parts)


# ─── Cached JSON loader ───────────────────────────────────────────────────────
@st.cache_data(show_spinner=False)
def load_data() -> dict:
    """Load portfolio_data.json once and cache for the session."""
    data_path = _path("portfolio_data.json")
    try:
        with open(data_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"⚠️ Could not load portfolio_data.json: {e}")
        return {}


# ─── CSS / HTML Injection ─────────────────────────────────────────────────────
def inject_css() -> None:
    """Inject the global CSS stylesheet (styles/main.css) and glow spotlights."""
    css_path = _path("styles", "main.css")
    if os.path.exists(css_path):
        with open(css_path, encoding="utf-8") as f:
            css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    # Glow spotlight divs (fixed/z-index:-1, no pointer-events)
    st.markdown(
        '<div class="glow-spotlight-1"></div><div class="glow-spotlight-2"></div>',
        unsafe_allow_html=True,
    )


def page_header(page_label: str) -> None:
    """Render the branded top navbar with the current page label."""
    data = load_data()
    name = data.get("personal_info", {}).get("name", "Portfolio")
    st.markdown(
        f"""
        <div class="navbar">
            <a class="navbar-brand" href="/">{name}<span>.</span></a>
            <div class="navbar-nav">
                <span class="page-badge">{page_label}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ─── Asset helpers ────────────────────────────────────────────────────────────
def file_to_base64(filepath: str) -> str | None:
    """Return base64-encoded string for a binary file, or None if not found."""
    full = _path(filepath)
    if not os.path.exists(full):
        return None
    with open(full, "rb") as f:
        return base64.b64encode(f.read()).decode()


# ─── Reusable HTML component builders ────────────────────────────────────────
def render_tech_badges(tags: list[str]) -> str:
    """Return HTML for a row of tech-badge spans."""
    return "".join(f'<span class="tech-badge">{tag}</span>' for tag in tags)


def render_skill_pills(skills: list[str], pill_class: str) -> str:
    """Return HTML for a group of skill pills."""
    return "".join(f'<span class="{pill_class}">{s}</span>' for s in skills)
