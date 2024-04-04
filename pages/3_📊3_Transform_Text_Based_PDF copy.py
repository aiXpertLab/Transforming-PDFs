from transformers import T5ForConditionalGeneration, T5Tokenizer
import streamlit as st
from utils import st_def, ut_tools as tb

st_def.st_logo(title='Welcome 👋 to Transformers PDF!', page_title="PDF Transformers",)
st_def.st_load_pdf()
#-------------------------------------------------
import PyPDF2, os

pdf_text_dir= st.session_state['pdf_text_dir']
pdf_files   = [file for file in os.listdir(pdf_text_dir) if file.endswith('.pdf')]

if pdf_files:
    for file_name in pdf_files:
        st.markdown("#### " + file_name)
        with open(os.path.join(pdf_text_dir, file_name), 'rb') as file:
            # Create a PDF reader object
            reader = PyPDF2.PdfReader(file)

            # Extract text from each page
            text = ''
            text_summaries =''
            for page in reader.pages:                text += page.extract_text()

            # Save the extracted text as a text file
            text_file_name = file_name.replace('.pdf', '.txt')
            text_file_path = os.path.join(st.session_state['text_dir'], text_file_name)
            with open(text_file_path, 'w') as text_file:    text_file.write(text)

            st.success(f"🌟Successfully transform PDF to text. Here is the first 300 characters: ")
            
            if st.button("Click button to Summarize", type="primary"):

                # Initialize the model and tokenizer
                model = T5ForConditionalGeneration.from_pretrained("t5-base")
                tokenizer = T5Tokenizer.from_pretrained("t5-base")

                # Encode the text
                inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1000, truncation=True)

                # Generate the summary
                outputs = model.generate(inputs, max_length=1000, min_length=100, length_penalty=2.0, num_beams=4, early_stopping=True)

                # Decode the summary
                summary = tokenizer.decode(outputs[0])
                text_summaries.append(summary)

        # Print the generated summaries for each resume
            for i, summary in enumerate(text_summaries):
                st.write(f"Summary for Resume {i+1}:")
                st.write(summary)

st.success(f"### 🌟Successfully transform all PDFs to text!")
                    
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
                    
