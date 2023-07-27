# Stock Analytics Dashboard

## Install Python Requirements

```bash
pip install -r requirements
```

## Usage

```bash
$ streamlit main.py
```

## Application Flow

## 📊 Technical analysis

This is a Python application that uses Streamlit to visualize historical stock data and various technical indicators for a selected stock. The application allows the user to input a ticker symbol and select a date range. It then fetches historical stock data using the Yahoo Finance API and calculates the following indicators:

* Exponential Moving Average (EMA)
* Relative Strength Index (RSI)
* Simple Moving Average (SMA)
* Moving Average Convergence Divergence (MACD)

The application provides an interactive web interface powered by Streamlit, where the user can adjust the parameters for each indicator to visualize their effects on the stock's historical data. The indicators are plotted alongside the stock's closing price, making it easier to analyze trends and potential trading signals.

### Usage
1. Select a stock by entering its ticker symbol (e.g., "META").
2. Choose the start date for the historical data using the date input widget.
3. The application will fetch the historical data for the selected stock and date range.
4. Use the sliders to adjust the parameters for each indicator:
    * EMA Period: Adjust the number of periods for the Exponential Moving Average.
    * RSI Period: Adjust the number of periods for the Relative Strength Index.
    * SMA Period: Adjust the number of periods for the Simple Moving Average.
5. The web application will display a table containing the historical stock data along with the calculated values for EMA, RSI, SMA MACD, Signal Line, and MACD Histogram.
6. The application will also display interactive plots showing the stock's closing price, EMA, SMA, RSI, and MACD indicators over the selected date range.


## 🕯 Candlestick charts

### Download the Data

* Download list of symbols in the Nasdaq 100 and S&P 500 from WikiPedia.
* For each symbol, download 10 days of data (open, high, low, close) using Python package [yfinance](https://pypi.org/project/yfinance/)
* For each symbol, download earnings data using Python package [yahooquery](https://yahooquery.dpguthrie.com).

### Scan Stock Symbols for Candlestick Patterns

* For each of the 60+ candlestick patterns, scan all the symbols looking for pattern matches.
* Create list of patterns and the relevant symbols.

### Streamlit Webapp

With a list of candlestick patterns and symbols matching those patterns:

* Create drop-down lists in Streamlit with name of candlestick pattern and the symbol.
* Upon selection of a pattern/symbol from the drop-down, load a TradingView chart.
* Create plot of earnings data using [Ploty Express](https://plotly.com/python/plotly-express/).

## 🔎 Ticker Search

1. **Importing Dependencies**: The code starts by importing the required libraries - streamlit and pandas.
2. **```search_company_by_name``` Function**: This function takes two parameters - a DataFrame (```df```) containing company data and a query (```query```) representing the company name to search for. It uses the ```str.contains``` method to filter the DataFrame based on the query. The function returns a DataFrame containing the search results with columns "Name" and "Symbol".
3. **```main``` Function**: This is the main function that runs the Streamlit application. It starts by setting the title of the web application to "🔎 Company Search".
4. **Loading Data**: The code loads data from the CSV file named "nasdaq_screener.csv" using ```pd.read_csv```. The DataFrame (```df```) contains company information with columns "Name" and "Symbol".
5. **User Input**: The application presents an input box using ```st.text_input```, allowing the user to enter a company name to search for.
6. **Searching and Displaying Results**: When the user enters a query and clicks Enter, the ```search_company_by_name function``` is called with the DataFrame (```df```) and the user's query. The search results are obtained and displayed in a table using ```st.dataframe```. If no matching companies are found, a warning message is displayed using ```st.warning```.
7. **Running the Application**: Finally, the main function (```main```) is called to execute the Streamlit application. The application runs in a web browser, and the user can interact with it by entering a company name to search.

Overall, the flow of the code follows these steps: importing libraries, defining functions, loading data, obtaining user input, processing the input to find matching companies, and displaying the results in an interactive web interface using Streamlit.


## 💸 Top financial news
This is a Python application that uses Streamlit and BeautifulSoup to scrape financial news headlines related to the Economy category from a specific website. The application fetches the headlines and their corresponding article links from the given URL and displays them in an interactive web interface using Streamlit. The headlines will be displayed as clickable links to the respective articles.

The *scraping* function fetches the web page content from the specified URL and extracts the headlines and corresponding article links. It filters out headlines with a length greater than 35 characters to display only relevant news. 
*The character limits ensures that hyperlinks other than headlines are not included in the list.*

