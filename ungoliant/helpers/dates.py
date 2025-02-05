from datetime import date
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import pandas_market_calendars as mcal

# Initialize the NYSE calendar
nyse = mcal.get_calendar('NYSE')

# List of durations
durations = ['1w', '1m', '3m', '1y', '5y']

# Current date
today = datetime.today()

def get_current_date():
    """
    Returns the current date in YYYY-MM-DD format.
    """
    return date.today().strftime("%Y-%m-%d")

# Function to calculate the date based on duration
def get_date_from_duration(today, duration):
    if duration.endswith('w'):  # Weeks
        weeks = int(duration[:-1])
        return today - timedelta(weeks=weeks)
    elif duration.endswith('m'):  # Months
        months = int(duration[:-1])
        return today - relativedelta(months=months)
    elif duration.endswith('y'):  # Years
        years = int(duration[:-1])
        return today - relativedelta(years=years)
    else:
        raise ValueError(f"Unsupported duration format: {duration}")

def get_closest_market_open_date(date_str):
    """
    Get the closest previous market open date for a given date string in 'y-m-d' format.
    
    Parameters:
        date_str (str): The input date in 'y-m-d' format.
    
    Returns:
        datetime: The closest previous market open date.
    """
    # Convert the input string to a datetime object
    date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # NYSE market schedule for a date range
    schedule = nyse.schedule(start_date=date - timedelta(days=7), end_date=date + timedelta(days=7))
    open_dates = schedule.index.to_pydatetime()  # Convert index to list of datetime objects
    
    # Check if the date is in the open dates
    if date in open_dates:
        return date
    else:
        # Find the closest previous open date
        closest_previous_date = max([d for d in open_dates if d <= date])
        return closest_previous_date

if __name__ == "__main__":
    print(get_current_date())
    print(get_closest_market_open_date(get_current_date()))



# # Calculate the dates
# dates = {duration: get_date_from_duration(today, duration) for duration in durations}

# # Adjust dates to closest market open
# market_open_dates = {duration: get_closest_market_open_date(date) for duration, date in dates.items()}

# # Print results
# for duration, market_open_date in market_open_dates.items():
#     print(f"{duration}: {market_open_date.strftime('%Y-%m-%d')}")






