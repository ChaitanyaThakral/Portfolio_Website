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
        youtube_video_id = "lO_XO1zSWTg"
        video_html = f"""
        <iframe 
            width="560" 
            height="320" 
            src="https://www.youtube.com/embed/{youtube_video_id}?autoplay=1&mute=1&loop=1&playlist={youtube_video_id}&controls=0&modestbranding=1&rel=0" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen
            style="border-radius: 20px;">
        </iframe>
        """
        
        st.markdown(video_html, unsafe_allow_html=True)

st.markdown(""" <br>
            <p style='font-size:20px; margin-bottom: 0.5rem;'>
            <strong>📁 View Source Code on GitHub:</strong>
            </p>""",unsafe_allow_html=True)
            
st.markdown(f"""
<div style='display: flex; margin-top: 0.5rem;'>
    <a href="https://github.com/ChaitanyaThakral/Itinerary-Planner" 
       target="_blank"
       style='text-decoration: none;'>
        <span style='background-color:#f0f2f6; padding:8px 16px; border-radius:20px; font-size:16px; color: black; transition: all 0.3s ease; display: inline-flex; align-items: center; gap: 8px;'>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
            Source Code GitHub Link
        </span>
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("""<br> <br>""", unsafe_allow_html=True)


st.header("Experience",divider=True)

with st.container():
    title_col, logo_col = st.columns([3, 1])
    
    with title_col:
        st.markdown(
            """
            <h2 style='margin-bottom: 5px;'>Data Science Intern – Paytm</h2>
            <p style='font-size:18px; margin-bottom: 15px;'>
            <i>May 2025 – August 2025 | Remote/India</i>
            </p>
            """,unsafe_allow_html=True)
    
    with logo_col:
        st.image("paytm.png", width=250)

st.markdown(
    """
    <p style='font-size:20px; margin-bottom: 10px;'>
    <strong>Key Contributions:</strong>
    </p>
    <div style='font-size:20px; '>
    • <strong style='font-size:20px;'>Income Estimation Tuning:</strong> Enhanced monthly income prediction accuracy by integrating lender feedback through the implementation of deviation bands and custom multipliers, ensuring predictions align more closely with actual expectations.<br><br>
    
    • <strong style='font-size:20px;'>LLM & OCR Research:</strong> Conducted a comprehensive evaluation of various large language models (LLMs) and optical character recognition (OCR) tools by analyzing their features, pricing, and performance, thereby supporting informed internal document processing decisions.<br>
    
    • <strong style='font-size:20px;'>Text Classification:</strong> Developed a streamlined process utilizing PaddleOCR for text extraction from documents, followed by application of an existing classifier to accurately differentiate between handwritten and printed text.<br>
    
    • <strong style='font-size:20px;'>Cheque Liveliness Detection:</strong> Achieved a significant improvement in cheque quality detection accuracy, increasing from 90.6% to 96.8% through the refinement of prompts utilized in LLM-based classification.<br>
    
    • <strong style='font-size:20px;'>Bank Statement Validation:</strong> Elevated the accuracy of completeness and validity checks on bank statements to over 92% and 95%, respectively, by enhancing the prompts provided to LLMs.<br>
    
    • <strong style='font-size:20px;'>Tool Evaluation:</strong> Evaluated the performance and usability of LiteLLM to assess its potential for integration into existing systems.<br>
    
    • <strong style='font-size:20px;'>Information Extraction with Document AI:</strong> Assessed the effectiveness of Mistral's Document AI for extracting key cheque details—such as account name, number, and IFSC code—by conducting thorough evaluations and assisting the team in making informed decisions.
    </div>
    """,unsafe_allow_html=True)

st.markdown("""<br> """, unsafe_allow_html=True)

st.header("Get In Touch With Me!",divider = True)

with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        contact_form = """
        <form action="https://formsubmit.co/cthakral6@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Enter your name" required style="width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;">
            <input type="email" name="email" placeholder="Enter your email address" required style="width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;">
            <textarea name="message" placeholder="Enter your message" required style="width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box; height: 120px; resize: vertical;"></textarea>
            <button type="submit" style="width: 100%; padding: 10px; background-color: rgb(34, 133, 41); color: white; border: none; border-radius: 5px; cursor: pointer;">Send Message</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        social_icons = """
        <div style="display: flex; justify-content: center; gap: 20px; margin-top: 20px;">
            <a href="mailto:cthakral6@gmail.com" style="text-decoration: none; color: #333;">
                <svg width="60" height="60" viewBox="0 0 24 24" fill="currentColor" style="transition: color 0.3s ease;">
                    <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
                </svg>
            </a>
            <a href="https://github.com/ChaitanyaThakral" target="_blank" style="text-decoration: none; color: #333;">
                <svg width="50" height="60" viewBox="0 0 24 24" fill="currentColor" style="transition: color 0.3s ease;">
                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
            </a>
            <a href="https://www.linkedin.com/in/chaitanyathakrai/" target="_blank" style="text-decoration: none; color: #333;">
                <svg width="50" height="60" viewBox="0 0 26 24" fill="currentColor" style="transition: color 0.3s ease;">
                    <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                </svg>
            </a>
        </div>
        """
        st.markdown(social_icons, unsafe_allow_html=True)



