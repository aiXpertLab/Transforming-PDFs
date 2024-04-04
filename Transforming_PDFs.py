import streamlit as st, shutil, os
from utils.st_def import st_main_contents, st_logo

st.session_state['pdf_image_dir']= './data/pdf/image_based_pdf_files'
st.session_state['pdf_text_dir'] = './data/pdf/text_based_pdf_files'
st.session_state['text_dir']     = './data/pdf/extracted_text'     # Directory for storing extracted text from PDFs
st.session_state['ocr_dir']      = './data/pdf/ocr_output'         # OCR output directory for scanned PDFs
st.session_state['pdf_d']     = './data/pdf'
if 'session_initialized' not in st.session_state:
    st.session_state.session_initialized = True     #new
    os.makedirs(st.session_state['pdf_d'], exist_ok=True)
    shutil.rmtree(st.session_state['pdf_d'])
    os.makedirs(st.session_state['pdf_image_dir'], exist_ok=True)
    os.makedirs(st.session_state['pdf_text_dir'] , exist_ok=True)
    os.makedirs(st.session_state['text_dir']     , exist_ok=True)
    os.makedirs(st.session_state['ocr_dir']      , exist_ok=True)

st_logo(title='Welcome 👋 to PDF Transformers !', page_title="PDF Transformers",)
st_main_contents()