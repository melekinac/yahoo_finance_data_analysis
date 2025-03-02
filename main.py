import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Enable interactive mode for displaying charts
plt.ion()

def get_multiple_stocks(tickers, start_date, end_date):
    """
    Retrieves historical stock data for multiple tickers from Yahoo Finance.

    Parameters:
    tickers (list): List of stock symbols (e.g., ['AAPL', 'TSLA'])
    start_date (str): Start date for data retrieval (YYYY-MM-DD format)
    end_date (str): End date for data retrieval (YYYY-MM-DD format)

    Returns:
    pandas.DataFrame: Stock data with adjusted prices
    """
    data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker', auto_adjust=True)
    
    # Reshape the data to handle multiple tickers properly
    data = data.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level='Ticker')
    return data

def calculate_indicators(data, tickers):
    """
    Calculates key financial indicators: daily return, moving averages, and volatility.

    Parameters:
    data (pandas.DataFrame): Stock data
    tickers (list): List of stock symbols

    Returns:
    dict: Dictionary containing processed data for each stock ticker
    """
    new_data = {}
    for ticker in tickers:
        df = data[data['Ticker'] == ticker].copy()  
        df['Daily Return'] = np.log(df['Close'] / df['Close'].shift(1))  # Logarithmic return
        df['50 MA'] = df['Close'].rolling(window=50).mean()  # 50-day moving average
        df['200 MA'] = df['Close'].rolling(window=200).mean()  # 200-day moving average
        df['Volatility'] = df['Daily Return'].rolling(window=30).std()  # 30-day standard deviation (volatility)
        new_data[ticker] = df
    return new_data

def plot_multiple_stocks(data, tickers):
    """
    Plots stock closing prices along with their 50-day and 200-day moving averages.

    Parameters:
    data (dict): Processed stock data
    tickers (list): List of stock symbols

    Displays:
    A matplotlib line chart with stock prices and moving averages
    """
    plt.figure(figsize=(14, 8))
    for ticker in tickers:
        df = data[ticker]
        plt.plot(df.index, df['Close'], label=f'{ticker} Close')
        plt.plot(df.index, df['50 MA'], label=f'{ticker} 50 MA', linestyle='--')
        plt.plot(df.index, df['200 MA'], label=f'{ticker} 200 MA', linestyle=':')
    
    plt.title('Stock Prices and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.show(block=True)

def plot_correlation(data, tickers):
    """
    Plots a heatmap showing the correlation of daily returns between different stocks.

    Parameters:
    data (dict): Processed stock data
    tickers (list): List of stock symbols

    Displays:
    A seaborn heatmap representing stock correlations
    """
    daily_returns = pd.DataFrame({ticker: data[ticker]['Daily Return'] for ticker in tickers})
    correlation_matrix = daily_returns.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Stock Correlation')
    plt.show(block=True)


# 🏦 User Inputs
tickers = input("Enter stock symbols separated by commas (e.g., AAPL,TSLA,GOOGL,AMZN): ").split(',')
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

# 📊 Data Retrieval & Processing
data = get_multiple_stocks(tickers, start_date, end_date)
data = calculate_indicators(data, tickers)

# 🔍 Sample Output
print(f"\nSample data for {tickers[0]}:\n")
print(data[tickers[0]].head())

# 📈 Plot Graphs
plot_multiple_stocks(data, tickers)
plot_correlation(data, tickers)
