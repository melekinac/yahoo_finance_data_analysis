# Yahoo Finance Data Analysis

This project analyzes the stock prices of major technology companies (**AAPL, TSLA, GOOGL, AMZN**) using data from Yahoo Finance. It includes visualization of **daily stock prices, moving averages, and correlation heatmaps**.

## Features

- **Download historical stock data** using `yfinance`
- **Calculate financial indicators:**
  - **Daily Return**
  - **50-day Moving Average (50 MA)**
  - **200-day Moving Average (200 MA)**
  - **Stock Volatility**
- **Visualize stock price trends with moving averages**
- **Stock return correlation heatmap**

---

## **Technologies Used**

- **Python 3.12**
- **Libraries:** `yfinance`, `pandas`, `numpy`, `matplotlib`, `seaborn`

---

## **Results**

### 1. Stock Prices and Moving Averages

This chart shows the **daily closing prices** of each stock along with its **50-day and 200-day moving averages**. It helps identify **trends and potential support/resistance levels**.

![Stock Prices](./images/stock_prices.png)

---

### 2. Stock Correlation Heatmap

This heatmap shows the correlation between the **daily returns** of the selected stocks. A higher value indicates a stronger relationship.

![Stock Correlation](./images/stock_correlation.png)

---

## **Installation & Usage**

1️⃣ Clone the repository:

```sh
git clone https://github.com/melek/yahoo-finance-analysis.git
cd yahoo-finance-analysis
```
