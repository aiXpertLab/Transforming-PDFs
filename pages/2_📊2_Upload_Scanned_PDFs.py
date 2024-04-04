import streamlit as st
from utils import st_def, ut_tools

st_def.st_logo(title=' 👋 Load Text-Based PDFs!', page_title="PDF Transformers",)
# st_def.st_load_pdf()

ut_tools.upload_save_files(st.session_state["pdf_image_dir"])
