import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import datetime as dt

#-------------------------------------------------------------------------------
# Simple Moving Average
#-------------------------------------------------------------------------------
def SMA(data, window=100):
    data['SMA_100'] = data['Close'].rolling(window=window).mean()
    return data

#-------------------------------------------------------------------------------
# Calculate Exponential Moving Average (EMA)
#-------------------------------------------------------------------------------
def EMA(data, window=20):
    data['EMA'] = data['Close'].ewm(span=window, adjust=False).mean()
    return data

#-------------------------------------------------------------------------------
# Calculate Relative Strength Index (RSI)
#-------------------------------------------------------------------------------
def RSI(data, window=14):
    diff = data['Close'].diff()
    gain = diff.mask(diff < 0, 0)
    loss = -diff.mask(diff > 0, 0)
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data

#-------------------------------------------------------------------------------
# Calculate Linear Regression using the least squares method
#-------------------------------------------------------------------------------
def linear_regression(data, window=14):
    x = np.arange(len(data))
    y = data['Close'].values

    # Create a matrix with x values and a column of ones for the intercept term
    X = np.column_stack((x, np.ones_like(x)))

    # Calculate the coefficients using the least squares method
    coeffs, _, _, _ = np.linalg.lstsq(X, y, rcond=None)

    # Calculate the regression line using the coefficients
    reg_line = X @ coeffs

    return reg_line
#-------------------------------------------------------------------------------
# Calculate MACD
#-------------------------------------------------------------------------------
def MACD(data, short_window=12, long_window=26, signal_window=9):
    """
    Calculate Moving Average Convergence Divergence (MACD) for a given window sizes.

    Args:
        data (DataFrame): Stock data.
        short_window (int): Window size for short-term EMA.
        long_window (int): Window size for long-term EMA.
        signal_window (int): Window size for signal line.

    Returns:
        DataFrame: Stock data with MACD, Signal_Line, and MACD_Hist columns added.
    """
    exp_short = data['Close'].ewm(span=short_window, adjust=False).mean()
    exp_long = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = exp_short - exp_long
    data['Signal_Line'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    data['MACD_Hist'] = data['MACD'] - data['Signal_Line']
    return data

#-------------------------------------------------------------------------------
# Calculate Linear Regression using the least squares method
#-------------------------------------------------------------------------------
def linear_regression(data, window=14):
    x = np.arange(len(data))
    y = data['Close'].values

    # Create a matrix with x values and a column of ones for the intercept term
    X = np.column_stack((x, np.ones_like(x)))

    # Calculate the coefficients using the least squares method
    coeffs, _, _, _ = np.linalg.lstsq(X, y, rcond=None)

    # Calculate the regression line using the coefficients
    reg_line = X @ coeffs

    return reg_line

#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------
def main():
    st.title("Historical Stock Data and Indicators")

    # Select the stock and date range
    st.header("Stock Selection")
    selected_ticker = st.text_input('Enter Ticker Symbol (e.g., META)', 'META')
    start_date = st.date_input("Select Start Date", value=dt.datetime(2021, 1, 1))
    end_date = dt.datetime.now()

    # Fetching the historical data for a selected stock and date range
    data = yf.download(selected_ticker, start=start_date, end=end_date)

    # Calculate Exponential Moving Average (EMA)
    ema_period = st.slider("Select EMA Period", min_value=5, max_value=50, value=20)
    data = EMA(data, window=ema_period)

    # Calculate Relative Strength Index (RSI)
    rsi_period = st.slider("Select RSI Period", min_value=5, max_value=30, value=14)
    data = RSI(data, window=rsi_period)

    # Calculate Simple Moving Average (SMA)
    sma_window = st.slider("Select SMA Period", min_value=5, max_value=100, value=100)
    data = SMA(data, window=sma_window)

    # Calculate Linear Regression for Closing Price
    data['Linear_Regression'] = linear_regression(data)

    # Calculate MACD
    data = MACD(data)

    # Display the DataFrame with EMA, RSI, SMA, MACD, Signal_Line, and MACD_Hist columns as a table in Streamlit app
    st.subheader("Historical Stock Data:")
    st.dataframe(data)

    st.header("Indicators")
    # Create four subplots with a ratio of 4:1:1:1
    fig, axs = plt.subplots(4, 1, figsize=(10, 14), sharex=True, gridspec_kw={'height_ratios': [4, 1, 1, 1]})

    # Plot the Closing Price, Exponential Moving Average (EMA), and Simple Moving Average (SMA) on the first subplot
    axs[0].plot(data.index, data['Close'], label='Closing Price', color='blue')
    axs[0].plot(data.index, data['EMA'], label=f'EMA ({ema_period} periods)', color='orange')
    axs[0].plot(data.index, data['SMA_100'], label=f'SMA ({sma_window} periods)', color='red')
    axs[0].plot(data.index, data['Linear_Regression'], label='Linear Regression', color='green', linestyle='dashed')
    axs[0].set_ylabel('Price')
    axs[0].set_title(f'{selected_ticker} - Closing Price, EMA, and SMA')
    axs[0].legend()

    # Plot the RSI on the second subplot
    axs[1].plot(data.index, data['RSI'], label=f'RSI ({rsi_period} periods)', color='purple')
    axs[1].axhline(y=30, color='g', linestyle='dashed')  # Add lower bound RSI threshold at 30
    axs[1].axhline(y=70, color='r', linestyle='dashed')  # Add upper bound RSI threshold at 70
    axs[1].set_xlabel('Date')
    axs[1].set_ylabel('RSI')
    axs[1].set_title(f'{selected_ticker} - RSI')
    axs[1].legend()

    # Plot the Linear Regressi on the third subplot
    axs[2].plot(data.index, data['Close'], label='Closing Price', color='blue')
    axs[2].plot(data.index, data['Linear_Regression'], label='Linear Regression', color='green', linestyle='dashed')
    axs[2].set_xlabel('Date')
    axs[2].set_ylabel('Price')
    axs[2].set_title(f'{selected_ticker} - Closing Price vs. Linear Regression')
    axs[2].legend()

    # Plot the MACD and Signal Line on the fourth subplot
    axs[3].bar(data.index, data['MACD_Hist'], label='MACD Hist', color='blue')
    axs[3].plot(data.index, data['MACD'], label='MACD', color='orange')
    axs[3].plot(data.index, data['Signal_Line'], label=f'Signal Line', color='green')
    axs[3].set_xlabel('Date')
    axs[3].set_ylabel('MACD')
    axs[3].set_title(f'{selected_ticker} - MACD')
    axs[3].legend()


    plt.tight_layout()

    st.pyplot(fig)

#-------------------------------------------------------------------------------
# Driver
#-------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
