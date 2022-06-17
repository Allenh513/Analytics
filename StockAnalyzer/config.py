from datetime import datetime as dt

s3_BUCKET_NAME = ''
DATA_PATH = ''
# intialize the years, pull will be run by year just in case
start_dates = [str(i) + "-01-01" for i in range(2007, 2022)]
end_dates = [str(i) + "-01-01" for i in range(2007, 2022)]

# add odd ones on the beginning and end
start_dates = ["2006-05-16"] + start_dates
end_dates = end_dates + [str(dt.strftime(dt.now(),'%Y-%m-%d'))]

# dict of the name for the output file and then query string for Yahoo Finance
TICKERS = {
    "SP500": "^GSPC",
    "TESLA": "TSLA",
    "APPLE": "AAPL",
    "MSFT": "MSFT",
    "GOOGLE": "GOOGL"
}