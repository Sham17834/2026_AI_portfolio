import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma 
from langchain_classic.chains import RetrievalQA
from pydantic import SecretStr

# Load the environment variables from the .env file
load_dotenv()

# Retrieve the API key from the environment
api_key_value = os.getenv("GROQ_API_KEY")

if not api_key_value:
    raise ValueError("API Key not found! Ensure your .env file is set up correctly.")

# Initialize the HuggingFace embeddings model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Set up the Chroma vector database
vector_db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

# Initialize the ChatGroq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile", 
    temperature=0.7,
    api_key=SecretStr(api_key_value) 
)

# Create the RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_db.as_retriever()
)

# Run the query
query = "What is the maternity leave duration in the 2022 amendment?"
response = qa_chain.invoke({"query": query})

print("\n--- Result ---")
print(response["result"])