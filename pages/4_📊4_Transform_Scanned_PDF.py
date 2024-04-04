import streamlit as st
from utils import st_def, ut_tools as tb

st_def.st_logo(title='Welcome 👋 to Transformers PDF!', page_title="PDF Transformers",)
st_def.st_load_pdf()
#-------------------------------------------------
import PyPDF2, os, pytesseract
from pdf2image import convert_from_path

pdf_image_dir= st.session_state['pdf_image_dir']
pdf_files   = [file for file in os.listdir(pdf_image_dir) if file.endswith('.pdf')]

if pdf_files:
    for file_name in pdf_files:
        st.markdown("#### " + file_name)
        file_ = os.path.join(pdf_image_dir, file_name)
        st.text(file_)
        images = convert_from_path(file_)
        for i, image in enumerate(images):      # i is pagenumber
            ocr_text = pytesseract.image_to_string(image).encode("utf-8")
            st.write("Page # {} - {}".format(str(i),ocr_text))

#             # Save the OCR output as a text file
#             ocr_file_name = file_name.replace('.pdf', '.txt')
#             ocr_file_path = os.path.join(st.session_state['ocr_dir'], ocr_file_name)
#             with open(ocr_file_path, 'w') as ocr_file:
#                 ocr_file.write(ocr_text)
                
#             st.success(f"🌟Successfully transform PDF to text. Here is the first 300 characters: ")
#             st.markdown(ocr_text)

# st.success(f"### 🌟Successfully transform all PDFs to text!")
                    
    # # Optional Step
    # for file_name in os.listdir(pdf_image_dir):
    #     if file_name.endswith('.pdf'):
    #         # Open the PDF file
    #         with Image.open(os.path.join(pdf_image_dir, file_name)) as img:
    #             # Perform OCR using pytesseract
    #             ocr_text = pytesseract.image_to_string(img, lang='eng')

    #             # Save the OCR output as a text file
    #             ocr_file_name = file_name.replace('.pdf', '.txt')
    #             ocr_file_path = os.path.join(ocr_directory, ocr_file_name)
    #             with open(ocr_file_path, 'w') as ocr_file:
    #                 ocr_file.write(ocr_text)
                    
