import streamlit as st
import base64

st.set_page_config(
    page_title="Chaitanya Thakral | Portfolio",
    layout="wide"
)

# Custom CSS for background and margins
st.markdown("""
    <style>
        .stApp {
            background-color: white;
        }

        .block-container {
            padding: 3rem 11rem 11rem 11rem;
            background-color: white;
        }

        [data-testid="stHeader"], [data-testid="stToolbar"] {
            background-color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.header("About Me", divider=True)

with st.container():
    text_col, spacer_col, image_col = st.columns([3.5, 0.3, 3]) 

    with text_col:  
        st.markdown("""
        <p style='font-size:20px;'>
        My name is Chaitanya Thakral, and I am a 20-year-old undergraduate student at the University of British Columbia (UBC) in Vancouver.
        I am currently in my third year, pursuing a Bachelor of Science in Statistics.
        </p>

        <p style='font-size:20px;'>
        From a young age, I have been fascinated by how computers operate behind the scenes. This early curiosity, combined with a strong interest in mathematics,
        led me to explore programming and data analysis. Over time, I discovered that I not only enjoy building projects, but I also want to create something meaningful.
        Whether it’s a project, an app, or a data model, my goal is to apply my knowledge to make a real-world impact.
        </p>

        <p style='font-size:20px;'>
        Outside of my studies, I enjoy swimming and working out at the gym. Staying physically active helps me maintain focus, think clearly, and achieve balance
        in both my personal life and my work.
        </p>
        <br>
        """, unsafe_allow_html=True)

    with spacer_col:
        st.empty()  

    with image_col:
        st.image("profile_photo.jpg", width=390)

st.header("Areas of Interest & Personal Traits",divider=True)
st.markdown("""
<div style='display: flex; flex-wrap: wrap; gap: 3rem; margin-top: 1rem;'>
    <span style='background-color:#f0f2f6; padding:8px 16px; border-radius:20px; font-size:16px;'>Swift Learner</span>
    <span style='background-color:#f0f2f6; padding:8px 16px; border-radius:20px; font-size:16px;'>Diligent</span>
    <span style='background-color:#f0f2f6; padding:8px 16px; border-radius:20px; font-size:16px;'>Team Player</span>
    <span style='background-color:#f0f2f6; padding:8px 16px; border-radius:20px; font-size:16px;'>Ambitious</span>
    <span style='background-color:#f0f2f6; padding:8px 16px; border-radius:20px; font-size:16px;'>Passionate</span>
    
</div>
""", unsafe_allow_html=True)

st.markdown("""<br>
            <br>""", unsafe_allow_html=True)


st.header("Resume",divider=True)
st.write("You can view or download my resume below:")


with open("Chaitanya_Thakral_Resume.docx", "rb") as f:
    resume_data = f.read()
    b64 = base64.b64encode(resume_data).decode()

st.markdown(f"""
<div style='display: flex; margin-top: 1rem;'>
    <a href="data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{b64}" 
       download="Chaitanya_Thakral_Resume.docx" 
       style='text-decoration: none;'>
        <span style='background-color:#f0f2f6; padding:8px 16px; border-radius:20px; font-size:16px; color: black;'>
            📄 Download Resume (.docx)
        </span>
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("""<br> <br>""", unsafe_allow_html=True)

st.header("Acquired skills and competencies",divider = True)

st.markdown("**Programming Languages**")

st.markdown("""
<div style='display: flex; flex-wrap: wrap; gap: 0.8rem; margin-top: 0.5rem;'>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>Python</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>Java</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>R</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>C++</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>C</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>DrRacket</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""<br> """, unsafe_allow_html=True)

st.markdown("**Tools & Technologies**")
st.markdown("""
<div style='display: flex; flex-wrap: wrap; gap: 0.8rem; margin-top: 0.5rem;'>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>Git</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>Excel</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>VS Code</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>Jupyter</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>Streamlit</span>
</div>
""", unsafe_allow_html=True)
st.markdown("""<br> """, unsafe_allow_html=True)

st.markdown("**Libraries & Frameworks**")
st.markdown("""
<div style='display: flex; flex-wrap: wrap; gap: 0.8rem; margin-top: 0.5rem;'>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>Pandas</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>NumPy</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>Matplotlib</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>Scikit-learn</span>
</div>
""", unsafe_allow_html=True)
st.markdown("""<br> """, unsafe_allow_html=True)

st.markdown("**Concepts**")
st.markdown("""
<div style='display: flex; flex-wrap: wrap; gap: 0.8rem; margin-top: 0.5rem;'>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>Object-Oriented Programming</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>Data Analysis</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>Statistical Modeling</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>Data Cleaning</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>Visualization</span>
    <span style='background-color:#f0f2f6; padding:6px 12px; border-radius:16px;'>Inference</span>
</div>
""", unsafe_allow_html=True)
st.markdown("""<br><br> """, unsafe_allow_html=True)

st.header("Portfolio Projects",divider= True)
with st.container():
    text_col, spacer_col, image_col = st.columns([3.5, 0.3, 3]) 

    with text_col:
        st.markdown(
            """
            <h2 style='margin-bottom: 10px;'>Travel Itinerary Planner</h2>
            <p style='font-size:20px;'>
            A Java-based desktop app for organizing and managing trips.
            <br><br>
            <strong>Features:</strong><br>
            • Create trips with destination, dates, and type (solo, family, business)<br>
            • Plan daily activities and manage flight/accommodation info<br>
            • Track packing checklist with status<br>
            • Set activity-level budgets and track expenses<br>
            • View daily and overall budget summaries<br>
            • Supports File I/O for saving and loading data<br>
            • Transparent event logging of user actions<br>
            • Swing-based UI with splash screen and visuals<br><br>
            <strong>Tools Used:</strong> <br>Java · Swing · File I/O  · OOP · Event Logging
            </p>
            """,
            unsafe_allow_html=True
        )

    with image_col:
        st.image("images/itinerary_ui.png", use_column_width=True)

