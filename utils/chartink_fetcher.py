import requests
from bs4 import BeautifulSoup

def get_chartink_stocks(screener_url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.get(screener_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        stock_tags = soup.select("table.table tr td a")
        stocks = [tag.text.strip() for tag in stock_tags if tag.text.strip()]
        return stocks[:10]  # Limit to top 10 stocks for safety

    except Exception as e:
        print(f"Error fetching Chartink stocks: {e}")
        return []
