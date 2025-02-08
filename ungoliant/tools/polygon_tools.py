from ungoliant.helpers.polygon import PolygonClient
from langchain_core.tools import BaseTool, StructuredTool
from pydantic import BaseModel, Field

pg = PolygonClient()

#---------------------------------------------------------

class OpenClosePriceInput(BaseModel):
    ticker: str = Field(description="The stock symbol of the company to get open and close price for on a specific date.")
    date: str = Field(description="The date to get the close price for - the format must be YYYY-MM-DD")

def get_open_close_price(ticker: str, date: str):
    return pg.get_open_close(ticker=ticker, date=date)

close_price_tool = StructuredTool(name="Get Stock Open and Close Price",
                                  args_schema=OpenClosePriceInput,
                                  description='Get the open and close price of a stock on a given date.',
                                  func=get_open_close_price)

#---------------------------------------------------------




def sp500_change(time_period: str):
    """
    Gets the change of the S&P index over a specific time period. Can be used to understand the market trend.
    
    :param time_period: The time period to get the change over. Will only accept: '1w', '1m', '3m', '1y', '5y'.
    
    Returns:
        The change in the S&P index over the time period.
    """
    if time_period not in ['1w', '1m', '3m', '1y', '5y']:
        raise ValueError("The time period must be one of: '1w', '1m', '3m', '1y', '5y'")
    
    url = f'https://api.polygon.io/v2/aggs/ticker/SPY/range/{time_period}/percent'
    response = PolygonClient().make_request(url)
    
    return response['results']

class SPPriceChange(BaseModel):
    time_period: str = Field(description="The time period to get the change over. Will only accept: '1w', '1m', '3m', '1y', '5y'.")

voo_change_tool = StructuredTool(name="Get SP500 Index Change Over Time",
                                  args_schema=SPPriceChange,
                                  description="Gets the change of the S&P index over a specific time period. Can be used to understand the market trend.",
                                  func=sp500_change)

if __name__ == "__main__":
    print(PolygonClient().get_open_close(ticker="AAPL", date="2024-01-05"))