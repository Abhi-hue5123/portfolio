"""Contact page."""

from __future__ import annotations

from urllib.parse import quote

import streamlit as st

from utils import load_data, page_intro, render_social_row

data = load_data()
info = data.get("personal_info", {})

page_intro(
    "09 - Contact",
    "Let's Talk",
    "Reach out about full-time roles, contract data engineering work, or just to say hello.",
    key="contact_intro",
)

info_col, form_col = st.columns([1, 1.4], gap="large")

with info_col:
    with st.container(key="contact_info_card"):
        st.subheader("Contact Details")

        badge = info.get("status_badge")
        if badge:
            st.badge(badge, color="green")

        if info.get("email"):
            st.write(f"**Email:** {info['email']}")
        meta_bits = [bit for bit in (info.get("location"), info.get("timezone")) if bit]
        if meta_bits:
            st.write(f"**Location:** {' · '.join(meta_bits)}")

        st.write("")
        st.caption("Find me elsewhere")
        render_social_row(info, key="contact_social_row")

with form_col:
    with st.container(key="contact_form_card"):
        st.subheader("Send a Message")
        st.caption("This drafts an email in your default mail client addressed to me — nothing is stored or sent from this site.")

        with st.form("contact_form", clear_on_submit=False):
            name = st.text_input("Your name")
            email = st.text_input("Your email")
            message = st.text_area("Message", height=160)
            submitted = st.form_submit_button("Prepare email", type="primary", width="stretch")

        if submitted:
            if not name or not email or not message:
                st.warning("Please fill in your name, email, and message.")
            else:
                subject = quote(f"Portfolio inquiry from {name}")
                body = quote(f"{message}\n\n— {name} ({email})")
                mailto = f"mailto:{info.get('email', '')}?subject={subject}&body={body}"
                st.success("Your message is ready — click below to send it from your email app.")
                st.link_button("Open email draft", mailto, type="primary", width="stretch")
