# 📈 Stock Trading Python App (Polygon API)

A beginner-friendly data pipeline project that fetches real-time stock market data from the Polygon.io API, converts it into a pandas DataFrame, and exports it as a CSV for further analysis or visualization.  

This project demonstrates API integration, environment variable handling, and clean data saving — foundational skills for Data Engineering and Data Analytics.

---

## Features
- Secure API key management using `.env`
- Real-time stock data retrieval (example: AAPL)
- JSON → pandas DataFrame → CSV pipeline
- Ready for visualization or database storage

---

## Tech Stack
- **Python 3.10+**
- **pandas**
- **requests**
- **python-dotenv**
- **Polygon.io API**

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mykeil-tzul/stock-trading-python-app.git
   cd stock-trading-python-app

2. **Create and activate a virtual environment**
   python3 -m venv venv
source venv/bin/activate  # (Mac/Linux)
venv\Scripts\activate     # (Windows)

3. **Install dependencies**
   pip install -r requirements.txt

4. **Set up your .env file**
   POLYGON_API_KEY=your_polygon_api_key_here

5. **Run the script**
   python script.py

# 💡 Learning Takeaways**

- Managing API keys securely with dotenv

- Making HTTP requests with requests

- Converting JSON to pandas DataFrame

- Saving data for analysis or visualization
