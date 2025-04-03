import streamlit as st
from llms import optimize_code
st.title("Code Optimizer")
st.write("Enter your code below")

# Code input box
code = st.text_area("Paste your code here", height=400)

# Optimize button
if st.button("Optimize Code"):
    if not code.strip():
        st.warning("Please enter some code first!")
    else:
        response = optimize_code(code)
        st.subheader("Optimized Code:")
        st.code(response, language="python")
