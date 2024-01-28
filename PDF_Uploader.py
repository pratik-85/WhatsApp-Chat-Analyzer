import streamlit as st
import os

st.title("📃PDF UPLOADER")
pdf_uploader = st.file_uploader(label="Upload an PDF", type=['pdf', 'txt'])
if pdf_uploader is not None:
    file_details = {"FileName": pdf_uploader.name, "FileType": pdf_uploader.type}
    st.write(file_details)
    
    with open(os.path.join("tempDir", pdf_uploader.name), "wb") as f:
        f.write(pdf_uploader.getbuffer())
        st.success("Saved File")
