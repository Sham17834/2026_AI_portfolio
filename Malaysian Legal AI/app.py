import streamlit as st
from rag_chain import qa_chain

# Streamlit app
st.title("Malaysia Labor Law AI")

# User input
user_q = st.text_input("Ask about Employment Act (e.g. Maternity Leave):")

# Process the query and get the answer
if user_q:
    with st.spinner("Searching..."):
        response = qa_chain.invoke({"query": user_q})
        
    st.subheader("Answer:")
    st.write(response["result"])