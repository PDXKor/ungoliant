import requests 
import os
from dotenv import load_dotenv

load_dotenv()
polygon_api_key = os.getenv("POLYGON_API_KEY")
base_url = os.getenv("OPEN_CLOSE_URL")

def get_close_on_date(date:str, ticker:str) -> int:
    """Gets the closing stock price for the stock on the latest trading day.

    Args:
        date: str - the date formatted as YYYY-MM-DD

    Returns:
        Last close price
    """
    url = f'{base_url}{ticker}/{date}'#/AAPL/"+date
    params = {
        "adjusted": "true",
        "apiKey": polygon_api_key,
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()  
    response = response.json()
    close = response['close']
    
    return close

if __name__ == "__main__":
    print(get_close_on_date("2021-01-04",ticker="AAPL"))