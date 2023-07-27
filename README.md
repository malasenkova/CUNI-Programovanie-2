## Stock Analytics Dashboard

## Install Python Requirements

```bash
pip install -r requirements
```

## Usage

```bash
$ streamlit main.py
```

## Subpage Flow

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
