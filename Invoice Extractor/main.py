# Load necessary libraries
import os
import json
import pandas as pd
from google import genai
from PIL import Image
from dotenv import load_dotenv

# Initialize environment and client
load_dotenv()
client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))

# Function to perform advanced extraction from receipt image
def start_advanced_extraction(image_path):
    img = Image.open(image_path)

    prompt = """
    Act as a Malaysian Tax Auditor. Analyze this receipt and extract structured data.
    
    RULES:
    1. Identify the 'Merchant Registration Number' (BRN) if available.
    2. Breakdown 'line_items' including description, quantity, and unit price.
    3. Identify 'SST_Type': Note if it is 6%, 8% (Service Tax), or 5%/10% (Sales Tax).
    4. Detect 'Payment_Method': Cash, e-Wallet (Grab/TNG), or Card.
    
    OUTPUT JSON SCHEMA:
    {
      "merchant": {"name": "str", "reg_no": "str", "address": "str"},
      "transaction": {"date": "YYYY-MM-DD", "time": "HH:MM", "invoice_no": "str"},
      "line_items": [{"desc": "str", "qty": 0, "price": 0.00, "total": 0.00}],
      "tax_summary": {"sst_rate": "percentage", "tax_amount": 0.00},
      "totals": {"subtotal": 0.00, "rounding": 0.00, "grand_total": 0.00},
      "payment": {"method": "str"}
    }
    """

    # Generate content using the Gemini model
    response = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = [prompt, img],
        config = {'response_mime_type': 'application/json'}
    )

    # Check if response is empty
    if not response.text:
        return
    
    # Parse the JSON response
    data = json.loads(response.text)
    
    # Save the extracted data to an Excel file
    with pd.ExcelWriter("outputs/invoice_data.xlsx") as writer:
        summary_df = pd.json_normalize(data)

        # Remove 'line_items' from summary if it exists to avoid redundancy
        if 'line_items' in summary_df.columns:
            summary_df.drop(columns = ['line_items'], inplace = True)
        
        summary_df.to_excel(writer, sheet_name = 'Summary', index = False)
        
        # Create a separate sheet for line items if they exist
        items_df = pd.DataFrame(data['line_items'])
        items_df.to_excel(writer, sheet_name = 'Line_Items', index = False)

# Run the extraction function
start_advanced_extraction("data/receipt1.jpg")