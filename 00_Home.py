import streamlit as st
import base64


def home():
    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Abhiram Singuru's Portfolio",
        page_icon="🧑‍💻",
    )

    # CSS styles file
    with open("styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open("assets/profile_squared.png", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

    # PDF CV file
    with open("assets/Abhiram_Singuru_CV.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Top title
    st.write(f"""<div class="title"><strong>Hi! My name is</strong> Abhiram Singuru👋</div>""", unsafe_allow_html=True)

    # Profile image
    st.write(f"""
    <div class="container">
        <div class="box">
            <div class="spin-container">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Abhiram Singuru">
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">Oracle PL/SQL Developer and Software Engineer</div>""", unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
        "LinkedIn": ["https://linkedin.com/in/abhiram-singuru11", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/Abhi-hue5123", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
        "Email": ["mailto:abhiramsinguru@gmail.com", "https://cdn-icons-png.flaticon.com/512/732/732200.png"],
    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", unsafe_allow_html=True)

    st.write("##")

    # About me section
    st.subheader("About Me")
    st.write("""
    - 🧑‍💻 I am a **Software Engineer** specializing in Oracle PL/SQL, Unix Shell Scripting, and Java.
    - 🛠️ Currently working as an **Associate** at Cognizant Technology Solutions, India.
    - ❤️ Passionate about **Cloud Computing (AWS)**, **Database Optimization**, and **Automation**.
    - 📫 How to reach me: abhiramsinguru@gmail.com
    - 🏠 Based in Visakhapatnam, India.
    """)

    st.write("##")

    # Skills section
    st.subheader("Technical Skills")
    st.write("""
    - **Programming Languages:** Oracle PL/SQL, Unix Shell Scripting, Java
    - **Databases:** Oracle 19c
    - **Cloud Platforms:** AWS (Amazon Web Services)
    - **Development Tools:** TOAD, VSCode IDE, WinSCP
    - **Version Control:** Git, GitHub
    - **Monitoring & Scheduling Tools:** Autosys, Dynatrace, Splunk
    """)

    st.write("##")

    # Work Experience section
    st.subheader("Work Experience")
    st.write("""
    - **Associate at Cognizant Technology Solutions, India (Oct 2021 - Present)**
        - Optimized Oracle PL/SQL procedures and packages for a legacy insurance application.
        - Resolved critical production issues and performed root cause analysis (RCA).
        - Collaborated with stakeholders to align solutions with business needs.
        - Designed automation workflows to reduce manual tasks and improve efficiency.
    """)

    st.write("##")

    # Certifications section
    st.subheader("Certifications")
    st.write("""
    - **Oracle Database SQL Certified Associate 1Z0-071** (02/2025)
    - **AWS Certified Cloud Practitioner** (08/2024 - 08/2027)
    - **Oracle Cloud Infrastructure 2024 Generative AI Certified Professional** (12/2024 - 12/2026)
    """)

    st.write("##")

    # Education section
    st.subheader("Education")
    st.write("""
    - **B.Tech in Electronics and Communication Engineering**
        - Gayatri Vidya Parishad College of Engineering (A), Visakhapatnam, India (July 2017 - July 2021)
    """)

    st.write("##")

    # Download CV button
    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="Abhiram_Singuru_CV.pdf",
        mime="application/pdf",
    )

    st.write("##")

    st.write(f"""<div class="subtitle" style="text-align: center;">⬅️ Check out my Projects in the navigation menu! (Coming soon...)</div>""", unsafe_allow_html=True)


if __name__ == "__main__":
    home()