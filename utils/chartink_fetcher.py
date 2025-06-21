import requests
from bs4 import BeautifulSoup

def get_chartink_stocks(screener_url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(screener_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        stocks = []

        for row in soup.select("table#DataTables_Table_0 tbody tr"):
            cols = row.find_all("td")
            if cols:
                symbol = cols[1].text.strip()
                stocks.append(symbol.upper())

        return stocks
    except Exception as e:
        print(f"⚠️ Error fetching Chartink data: {e}")
        return []
