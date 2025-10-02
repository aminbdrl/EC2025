import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Resume", page_icon="📄", layout="wide")

# --- HEADER ---
col1, col2 = st.columns([1, 3])
with col1:
    st.image("gambar amin.png", width=180)

with col2:
    st.markdown(
        """
        # **MUHAMMAD AMINUDDEEN BIN BADROL HISHAM**
        #### Aspiring Data Scientist | Artificial Intelligence 
        📍 No.3, Lorong Azzaharah 10/4b, 42300, Bandar Puncak Alam, Selangor  
        📧 **Email:** [maminuddeenh@gmail.com](mailto:maminuddeenh@gmail.com)  
        📞 **Phone:** +60 105-341-583  
        🔗 [LinkedIn](https://www.linkedin.com/in/muhammad-aminuddeen-820a9a189/)
        """
    )

st.write("---")

# --- EDUCATION ---
st.markdown("## 🎓 Education")
st.markdown(
    """
    **Bachelor of Information Technology with Honours** | *2023 - 2026*  
    - Relevant Coursework: Machine Learning, Artificial Intelligence, Computer Evaluation  
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
        - Designed and maintained web applications using HTML & CSS.  
        - Assisted with admin tasks including inventory tracking.  
        - Improved workflow efficiency by **15%** through process automation.  
        """
    )

# --- SKILLS ---
st.markdown("## 🛠️ Skills")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Programming:**\n- Python\n- SQL\n- JavaScript")
with col2:
    st.markdown("**Data & ML:**\n- Machine Learning\n- Data Visualization\n- Excel")
with col3:
    st.markdown("**Web & Tools:**\n- HTML, CSS\n- GitHub\n- Notepad++")

# --- PROJECTS ---
st.markdown("## 🚀 Projects & Achievements")
st.markdown(
    """
    **Crypto Price Prediction Model**  
    - Built regression models (Linear Regression, Decision Tree) to predict crypto prices.  
    - Achieved **MSE score: 0.93**.  

    **Flood Risk Prediction Model**  
    - Developed regression model for predicting flood risks in Kelantan.  
    - Evaluated using **MSE, MAE, RMSE**.  

    **Nestworks (IoT + AI)**  
    - Automated Poultry Feeding & Growth Tracking System.  

    🏆 **1st Runner Up – LionLair Hotlink International Techno Connect 2025**
    """
)

# --- FOOTER ---
st.write("---")
st.caption("© 2025 Aminuddeen | Built with Streamlit")
