import streamlit as st
import PyPDF2

def extract_text_from_pdf(uploaded_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()
    return text

def main():
    st.title("Cheque Text Extraction")

    st.write("Upload a PDF file containing a cheque to extract the text.")

    uploaded_file = st.file_uploader("Choose a file", type=["pdf"])

    if uploaded_file is not None:
        text = extract_text_from_pdf(uploaded_file)
        st.subheader("Extracted Text:")
        st.text(text)

if __name__ == "__main__":
    main()