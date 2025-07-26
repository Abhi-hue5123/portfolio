import streamlit as st
import base64


def home():
    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Abhiram Singuru's Portfolio",
        page_icon="🧑‍💻",
        layout="wide",  # Enables a wide layout for the grid
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

    # Create a grid layout
    col1, col2 = st.columns([1, 2])  # Left column (1 part) and right column (2 parts)

    # Left column: Name, title, picture, and contact links
    with col1:
        # Profile image
        st.write(f"""
        <div class="container">
            <div class="box">
                <div class="spin-container">
                    <div class="shape">
                        <div class="bd">
                            <img src="{img}" alt="Abhiram Singuru" style="width: 100%; border-radius: 50%;">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Name and title
        st.write(f"""<h1 style="text-align: center;">Abhiram Singuru</h1>""", unsafe_allow_html=True)
        st.write(f"""<h3 style="text-align: center; color: gray;">Oracle PL/SQL Developer</h3>""", unsafe_allow_html=True)

        # Social Icons
        social_icons_data = {
            "LinkedIn": ["https://linkedin.com/in/abhiram-singuru11", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
            "GitHub": ["https://github.com/Abhi-hue5123", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
            "Email": ["mailto:abhiramsinguru@gmail.com", "https://cdn-icons-png.flaticon.com/512/732/732200.png"],
        }

        social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}' style='width: 30px; height: 30px;'></a>" for platform in social_icons_data]

        st.write(f"""
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            {''.join(social_icons_html)}
        </div>""", unsafe_allow_html=True)

        # Download CV button (center-aligned and styled)
        st.write(f"""
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <a href="data:application/pdf;base64,{base64.b64encode(pdf_bytes).decode()}" download="Abhiram_Singuru_CV.pdf" style="text-decoration: none;">
                <button style="
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    text-align: center;
                    font-size: 16px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                ">
                    Download CV
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)


    # Right column: About me, skills, certifications, education, and CV download
    with col2:
        # About me section
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("About Me")
        st.write("""
        - 🧑‍💻 I am a **Software Engineer** specializing in Oracle PL/SQL, Unix Shell Scripting, and Java.
        - 🛠️ Currently working as an **Associate** at Cognizant Technology Solutions, India.
        - ❤️ Passionate about **Cloud Computing (AWS)**, **Database Optimization**, and **Automation**.
        - 📫 How to reach me: abhiramsinguru@gmail.com
        - 🏠 Based in Hyderabad, India.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

        # Skills section
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("Technical Skills")
        st.write("""
        - **Programming Languages:** Oracle PL/SQL, Unix Shell Scripting, Java
        - **Databases:** Oracle 19c
        - **Cloud Platforms:** AWS (Amazon Web Services)
        - **Development Tools:** TOAD, VSCode IDE, WinSCP
        - **Version Control:** Git, GitHub
        - **Monitoring & Scheduling Tools:** Autosys, Dynatrace, Splunk
        """)
        st.markdown('</div>', unsafe_allow_html=True)

        # Certifications section
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("Certifications")
        st.write("""
        - **Oracle Database SQL Certified Associate 1Z0-071** (02/2025)
        - **AWS Certified Cloud Practitioner** (08/2024 - 08/2027)
        - **Oracle Cloud Infrastructure 2024 Generative AI Certified Professional** (12/2024 - 12/2026)
        """)
        st.markdown('</div>', unsafe_allow_html=True)

        # Education section
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("Education")
        st.write("""
        - **B.Tech in Electronics and Communication Engineering**
            - Gayatri Vidya Parishad College of Engineering (A), Visakhapatnam, India (July 2017 - July 2021)
        """)
        st.markdown('</div>', unsafe_allow_html=True)

        # # Download CV button
        # st.markdown('<div class="section">', unsafe_allow_html=True)
        # st.download_button(
        #     label="📄 Download my CV",
        #     data=pdf_bytes,
        #     file_name="Abhiram_Singuru_CV.pdf",
        #     mime="application/pdf",
        # )
        # st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    home()