from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Load the PDF document and split it into pages
loader = PyPDFLoader("data/Akta Kerja 1955.pdf")
pages = loader.load_and_split()

# Create embeddings for the pages and store them in a Chroma vector database
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_db = Chroma.from_documents(pages, embeddings, persist_directory="./chroma_db")