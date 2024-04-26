import streamlit as st
from use_model import get_category
from io import StringIO  
import os
from extract_text_pdf import get_text

st.title("Resume Screening App")
image_file = st.file_uploader("Upload Resume", type=["pdf", "txt"])
if image_file is not None:
    with open(os.path.join("tempDir", "temp-file.pdf"),"wb") as f: 
      f.write(image_file.read())         
    st.success("Saved File")

    text = get_text("tempDir/temp-file.pdf")
    category = get_category(text)
    st.success("Category: " + category)