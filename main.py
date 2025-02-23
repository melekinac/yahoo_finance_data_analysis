import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


plt.ion()


def get_multiple_stocks(tickers, start_date, end_date):
    """It pulls specific shares and aggregates them into a single DataFrame."""
    data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker', auto_adjust=True)
   
    data = data.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level='Ticker')
    return data


def calculate_indicators(data, tickers):
    """Calculates daily return, moving average and volatility for each stock."""
    new_data = {}
    for ticker in tickers:
        df = data[data['Ticker'] == ticker].copy()  
        df['Daily Return'] = np.log(df['Close'] / df['Close'].shift(1))
        df['50 MA'] = df['Close'].rolling(window=50).mean()
        df['200 MA'] = df['Close'].rolling(window=200).mean()
        df['Volatility'] = df['Daily Return'].rolling(window=30).std()
        new_data[ticker] = df
    return new_data


def plot_multiple_stocks(data, tickers):
    """Shows closing prices and moving averages of multiple stocks on a single chart."""
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
    """It shows the correlation of returns between stocks with a heat map."""
    daily_returns = pd.DataFrame({ticker: data[ticker]['Daily Return'] for ticker in tickers})
    correlation_matrix = daily_returns.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Stock Correlation')
    plt.show(block=True)


tickers = ['AAPL', 'TSLA', 'GOOGL', 'AMZN']
start_date = '2023-01-01'
end_date = '2024-01-01'

data = get_multiple_stocks(tickers, start_date, end_date)
data = calculate_indicators(data, tickers)

print(data['AAPL'].head())  

plot_multiple_stocks(data, tickers)  
plot_correlation(data, tickers)      
