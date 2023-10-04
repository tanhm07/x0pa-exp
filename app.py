import streamlit as st
import PyPDF2
from io import BytesIO

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def score_cv_against_job_description(cv_text, job_description):
    cv_keywords = set(cv_text.lower().split())
    job_keywords = set(job_description.lower().split())
    overlap = cv_keywords.intersection(job_keywords)
    score = len(overlap) / len(job_keywords)
    return score

st.title("CV Scoring App")

uploaded_files = st.file_uploader("Upload CVs in PDF format", type="pdf", accept_multiple_files=True)

job_description = st.text_area("Enter the job description")

if uploaded_files and job_description:
    scores = {}
    for file in uploaded_files:
        pdf_file = BytesIO(file.read())
        extracted_text = extract_text_from_pdf(pdf_file)
        file_score = score_cv_against_job_description(extracted_text, job_description)
        scores[file.name] = file_score

    # Sort scores in descending order
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    for filename, score in sorted_scores:
        st.write(f"CV: {filename} | Score: {score:.2f}")

