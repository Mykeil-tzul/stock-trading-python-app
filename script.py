from dotenv import load_dotenv
import os
import requests
import pandas as pd

# --- Load environment variables ---
load_dotenv()  # Loads .env file
api_key = os.getenv("POLYGON_API_KEY")
print("Loaded API key:", api_key)

# --- Define the Polygon API endpoint ---
url = f"https://api.polygon.io/v2/aggs/ticker/AAPL/prev?adjusted=true&apiKey={api_key}"

# --- Send request to Polygon ---
response = requests.get(url)
data = response.json()

# --- Display top-level keys to confirm response structure ---
print("Keys in response:", data.keys())

# --- Print first ticker result if available ---
if "results" in data and data["results"]:
    print("First ticker:", data["results"][0])

    # --- Save data to CSV ---
    df = pd.DataFrame(data["results"])
    df.to_csv("aapl_data.csv", index=False)
    print("✅ Data saved to aapl_data.csv")

else:
    print("⚠️ No results found. Check API key or URL.")





