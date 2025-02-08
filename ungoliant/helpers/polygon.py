import requests 
import os
from dotenv import load_dotenv
from typing import Optional, Dict, Any
from ungoliant.helpers.logger import LoggingMixin

load_dotenv()

class PolygonClient(LoggingMixin):
    """
    A class to manage API calls to the Polygon service.
    """
    def __init__(self, api_key: str = None, base_url:str=None, timeout: int = 10):
        """
        Initialize the Polygon service client.

        :param api_key: The API key for the Polygon service.
        :param timeout: Default timeout for requests in seconds.
        """
        if not api_key:
            self.api_key = os.getenv("POLYGON_API_KEY")
        else: 
            self.api_key = api_key
        
        if not base_url:
            self.base_url = os.getenv("POLYGON_API_URL")
        else:
            self.base_url = base_url

        super().__init__(logger_name="PolygonLog", log_file="ungoliant/logs/polygon.log")

    def make_request(self, url, params:Optional[Dict[str, Any]] = None) -> Any:
        """Calls polygon API and returns the response"""
        if not params:
            params = {
                "adjusted": "true",
                "apiKey": self.api_key,
            }
        response = requests.get(url, params=params)
        response.raise_for_status()  
        response = response.json()
        
        self.log_info(f"Request made to {url} with params {params}")
        self.log_info(f"Response received: {response}")
        
        return response


    def get_open_close(self, date:str, ticker:str) -> Dict[float, float]:
        """
        Gets the closing stock price for the stock on the latest trading day.

        :param date: str - the date formatted as YYYY-MM-DD

        Returns:
            A response in the form of a dictionary. 
        """
        url = f'{self.base_url}open-close/{ticker}/{date}'     
        response = self.make_request(url)

        close = float(response['close'])
        open = float(response['open'])
        
        return response #{#"close": close, "open": open}



if __name__ == "__main__":
    print(PolygonClient().get_open_close("2021-01-04",ticker="AAPL"))