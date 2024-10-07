from yahoo_fin import stock_info as si

"""
previous code without try/except error handling



tickers = ["amzn", "meta", "goog",
    "not_a_real_ticker",
    "msft", "aapl", "nflx"]

all_data = {}
for ticker in tickers:
    all_data[ticker] = si.get_data(ticker)

"""
# modified code using except AssertionError
tickers = ["amzn", "meta", "goog",
    "not_a_real_ticker",
    "msft", "aapl", "nflx"]

all_data = {}
failures = []

for ticker in tickers:

    try:
        all_data[ticker] = si.get_data(ticker)
        print(ticker + "dowloaded sucessfully")
    
    except AssertionError:
        failures.append(ticker)
        print(ticker + "download failed")
