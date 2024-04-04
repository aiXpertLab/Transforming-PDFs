import os, streamlit as st

            
def upload_save_files(folder):
    uploaded_files = st.file_uploader("Upload PDF", type=["pdf"], accept_multiple_files=True)

    if uploaded_files:
        for uploaded_file in uploaded_files:
            if uploaded_file is not None:
                file_path = os.path.join(folder, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.success(f"🌟Successfully uploaded file: {uploaded_file.name}")
