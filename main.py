#-------------------------------------------------------------------------------
# Driver code for the Streamlit app
# streamlit run filename.py to run the code
#-------------------------------------------------------------------------------
import streamlit as st
import stock_performance as stock_performance
import candlestick as candlestick
import tickers as tickers
import news as news

#-------------------------------------------------------------------------------
# Set page configuration
#-------------------------------------------------------------------------------
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")

#-------------------------------------------------------------------------------
# Define page titles and URLs
#-------------------------------------------------------------------------------
pages = {
    "📊 Technical analysis": stock_performance,
    "🕯 Candlestick charts": candlestick,
    "🔎 Ticker Search": tickers,
    "💸 Top financial news": news
}

#-------------------------------------------------------------------------------
# Sidebar navigation
#-------------------------------------------------------------------------------
selected_page = st.sidebar.radio("Navigation", list(pages.keys()))

#-------------------------------------------------------------------------------
# Page selection
#-------------------------------------------------------------------------------
page = pages[selected_page]
page.main()
