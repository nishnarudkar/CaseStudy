import streamlit as st
from query_engine import process_query
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Streamlit app
st.title("Health Data Analysis with GenAI")
st.write("Upload datasets and ask health-related questions.")

# File upload
uploaded_file1 = st.file_uploader("Upload Health Dataset 1 (CSV)", type="csv")
uploaded_file2 = st.file_uploader("Upload Health Dataset 2 (CSV)", type="csv")

if uploaded_file1 and uploaded_file2:
    query = st.text_input("Enter your query:")
    if st.button("Generate Insights"):
        with st.spinner("Processing your query..."):
            insights = process_query(query, uploaded_file1, uploaded_file2)
            st.write("**Insights:**")
            st.write(insights)
