import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Resume", page_icon="📄", layout="wide")

# --- HEADER ---
col1, col2 = st.columns([1, 3])

with col1:
    st.image("gambar amin.png", width=180)  

with col2:
    st.markdown(
        
st.header("👤 Personal Information")
st.subheader("MUHAMMMAD AMINUDDEEN BIN BADROL HISHAM")
st.write("""
- 📍 Location: No.3,Lorong Azzaharah 10/4b, 42300, Bandar Puncak Alam, Kuala Selangor, Selangor
- 📧 Email: maminuddeenh@gmail.com
- 📞 Phone: +60 105-341-583  
- 🔗 LinkedIn: [LinkedIn](https://www.linkedin.com/in/muhammad-aminuddeen-820a9a189/)  
"""))

st.write("---")

# --- EDUCATION ---
st.markdown("## 🎓 Education")
st.markdown(
    """
    **Bachelor of Information Technology with Honours**  
     | *2023 - 2026*  
    - Relevant Coursework: Machine Learning, Artificial Intelligence, Computer Evoluation  
    - GPA: **3.4 / 4.0**
    """
)

# --- WORK EXPERIENCE ---
st.markdown("## 💼 Work Experience")

col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("**May 2022 – Dec 2022**")
with col2:
    st.markdown(
        """
        **Sub Admin | BroAutoPaintGarage**  
        - Developed and maintained web applications using HTML and CSS.  
        """
    )



# --- SKILLS ---
st.markdown("## 🛠️ Skills")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("- Python\n- SQL\n- Machine Learning")
with col2:
    st.markdown("- Data Visualization\n- Excel")
with col3:
    st.markdown("- Web Development (HTML, CSS, JS)\n- Cloud Platforms (Notepad++)")

# --- PROJECTS ---
st.markdown("## 🚀 Projects & Achievements")
st.markdown(
    """
    **Crypto Price Prediction Model**  
    - Built regression models (Linear Regression, Decision Tree) to predict crypto prices.  
    - Achieved MSE score of **0.93**.  

    **Flood Risk Prediction Model**  
    - Built regression models (Linear Regression) to predict flood in Kelantan.  
    - Used MSE,MAE and RMSE score.

    **Nestworks**
    - Build Automated Feeding & Growth Tracking System for Poultry
    - Method (IOT, AI)
 
    🏆 LionLair 1st Runner Up – Hotlink International Techno Connect 2025 
    """
)

# --- FOOTER ---
st.write("---")
st.caption("© 2025 Aminuddeen | Built with Streamlit")

