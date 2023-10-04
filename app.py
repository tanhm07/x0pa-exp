
import streamlit as st
import PyPDF2
from io import BytesIO

def extract_text_from_pdf(pdf_file):
    # Use PyPDF2's PdfReader to extract text from the uploaded PDF.
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

st.title("CV Scoring App")

uploaded_file = st.file_uploader("Upload your CV in PDF format", type="pdf")

if uploaded_file:
    # Convert the uploaded file to a BytesIO object to be processed by PyPDF2.
    pdf_file = BytesIO(uploaded_file.read())
    
    extracted_text = extract_text_from_pdf(pdf_file)
    st.write("Extracted Text from CV:")
    st.write(extracted_text)

def score_cv_against_job_description(cv_text, job_description):
    cv_keywords = set(cv_text.lower().split())
    job_keywords = set(job_description.lower().split())
    overlap = cv_keywords.intersection(job_keywords)
    score = len(overlap) / len(job_keywords)
    return score

job_description = st.text_area("Enter the job description")
if uploaded_file and job_description:
    score = score_cv_against_job_description(extracted_text, job_description)
    st.write(f"CV Score: {score:.2f}")
