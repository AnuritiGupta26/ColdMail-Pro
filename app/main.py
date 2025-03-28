
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(llm, portfolio, clean_text):
    # Apply Custom CSS for Theme
    st.markdown(
        """
        <style>
            body {
                background-color: #F7E6FF;
                color: #4A235A;
            }
            .stTextInput>div>div>input {
                background-color: #FFEEF7;
                color: black;
                border-radius: 10px;
                border: 2px solid #D291BC;
                padding: 10px;
            }
            .stButton>button {
                background-color: #D291BC;
                color: white;
                border-radius: 10px;
                padding: 10px;
                border: none;
                font-size: 16px;
            }
            .stButton>button:hover {
                background-color: #BA68C8;
            }
            .email-box {
                background-color: white;
                color: black !important;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            }
            a {
                color: black !important;
                font-weight: bold;
                text-decoration: none;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("📧 Cold Mail Generator")
    url_input = st.text_input(
        "🔗 Enter a Job URL:",
        value="https://weworkremotely.com/remote-jobs/orca-international-freelancer-remote-graphic-designer",
    )
    submit_button = st.button("✨ Generate Email")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            
            if not jobs:
                st.error("❌ No job details found. Please check the URL and try again.")
                return
            
            for job in jobs:
                skills = job.get("skills", [])
                
                if not skills:
                    continue  # Skip if no skills are found
                
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                
                if email:
                    st.markdown('<div class="email-box">' + email + '</div>', unsafe_allow_html=True)
                else:
                    st.error("⚠️ Failed to generate email. Please try again.")
        
        except Exception as e:
            st.error(f"❌ An Error Occurred: {e}")

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)
