
# AI-Powered Malaysian Financial & Legal Toolkit

This repository features a suite of AI applications designed to automate financial documentation and legal research specifically for the Malaysian market. By integrating **Google Gemini** and  **LangChain** , these tools provide high-accuracy, production-ready solutions for local tax and employment law inquiries.

---

### Key Applications

#### 1. Malaysian Receipt Extractor

An intelligent data extraction system that converts receipt images into structured, tax-compliant financial records.

* **Tax Compliance:** Automatically identifies Malaysian  **SST Types** , including 6%, 8% (Service Tax), and 5%/10% (Sales Tax).
* **Merchant Intelligence:** Extracts local Business Registration Numbers (BRN) and merchant addresses.
* **Payment Detection:** Specifically recognizes local payment methods such as  **GrabPay and Touch 'n Go (TNG)** .
* **Excel Integration:** Outputs data into a multi-sheet **Excel workbook** (`invoice_data.xlsx`) categorized by transaction summaries and line items.

#### 2. Malaysia Legal AI (Employment Act RAG Chatbot)

A Retrieval-Augmented Generation (RAG) chatbot developed to provide precise answers regarding the  **Malaysian Employment Act 1955** .

* **Legal Precision:** Uses the *Akta Kerja 1955* as the authoritative knowledge base to ensure responses are grounded in local law.
* **Hallucination Mitigation:** Employs **ChromaDB** for vector-based retrieval, ensuring the AI only references verified document snippets.
* **Streamlined UI:** Features a clean, interactive **Streamlit** interface for easy user navigation.

**Interface Preview:**
![Streamlit Interface](Malaysia%20Legal%20AI/picture/Streamlit_example.png)

---

### Technical Architecture

The toolkit is built on a modern AI stack optimized for Malaysian context-aware processing:

* **LLMs:** Google Gemini, Groq
* **Orchestration:** LangChain
* **Vector Store:** ChromaDB
* **Frontend:** Streamlit
* **Data Handling:** Pandas (Excel generation), PyPDF (Legal document parsing)
