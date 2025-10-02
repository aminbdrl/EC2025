import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Resume", page_icon="📄", layout="wide")

# --- HEADER ---
col1, col2 = st.columns([1, 3])

with col1:
    st.image("amin.jpeg", width=180)  

with col2:
    st.markdown(
        """
        # Your Full Name
        #### 📍 Location: Kuala Lumpur, Malaysia  
        📧 **Email:** your.email@example.com | 📞 **Phone:** +60 123-456-789  
        🔗 [LinkedIn](https://linkedin.com/in/yourprofile) | 🌐 [Portfolio](https://yourwebsite.com)
        """
    )

st.write("---")

# --- EDUCATION ---
st.markdown("## 🎓 Education")
st.markdown(
    """
    **Bachelor of Science in Computer Science**  
    University Name | *2018 - 2022*  
    - Relevant Coursework: Machine Learning, Data Science, Software Engineering  
    - GPA: **3.8 / 4.0**
    """
)

# --- WORK EXPERIENCE ---
st.markdown("## 💼 Work Experience")

col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("**Jan 2023 – Present**")
with col2:
    st.markdown(
        """
        **Software Engineer | Company Name**  
        - Developed and maintained web applications using Python and React.  
        - Collaborated with cross-functional teams to improve workflows.  
        - Automated deployment pipelines, reducing release time by 30%.
        """
    )

col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("**Jun 2022 – Dec 2022**")
with col2:
    st.markdown(
        """
        **Data Analyst Intern | Company Name**  
        - Analyzed customer data to provide actionable insights.  
        - Built dashboards with Tableau and Power BI.  
        - Improved reporting efficiency by 25%.
        """
    )

# --- SKILLS ---
st.markdown("## 🛠️ Skills")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("- Python\n- SQL\n- Machine Learning")
with col2:
    st.markdown("- Data Visualization\n- Excel / Power BI\n- Git & GitHub")
with col3:
    st.markdown("- Web Development (HTML, CSS, JS)\n- Streamlit\n- Cloud Platforms (AWS/GCP)")

# --- PROJECTS ---
st.markdown("## 🚀 Projects & Achievements")
st.markdown(
    """
    **Crypto Price Prediction Model**  
    - Built regression models (Linear Regression, Decision Tree) to predict crypto prices.  
    - Achieved R² score of **0.87**.  

    **Portfolio Website**  
    - Created a personal website using React & Tailwind.  
    - Showcased resume, projects, and blog posts.  

    🏆 *Dean’s List for 4 consecutive semesters*  
    🏆 *Hackathon Winner – Smart City Challenge 2021*
    """
)

# --- FOOTER ---
st.write("---")
st.caption("© 2025 Your Name | Built with Streamlit")

