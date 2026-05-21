import streamlit as st
import streamlit.components.v1 as components

# Sets the viewport to wide mode
st.set_page_config(layout="wide")

# Hides all Streamlit default headers, footers, and margins
st.markdown("""
    <style>
        header, footer, #MainMenu { visibility: hidden; }
        .block-container { padding: 0rem; }
    </style>
    """, unsafe_allow_html=True)

try:
    # 1. Read the HTML file
    with open("index.html", "r", encoding='utf-8') as f:
        html_content = f.read()
        
    # 2. Read the CSS file
    with open("style.css", "r", encoding='utf-8') as f:
        css_content = f.read()

    # 3. Inject the CSS directly into the HTML head so everything renders correctly
    styled_html = html_content.replace(
        '<link rel="stylesheet" href="style.css" />',
        f'<style>{css_content}</style>'
    )
    
    # 4. Display the complete birthday app
    components.html(styled_html, height=900, scrolling=True)

except FileNotFoundError as e:
    st.error(f"Missing file error: {e.filename}. Please check your repository.")
