import streamlit as st
import pandas as pd

#-------------------------------------------------------------------------------
# Search for companies by name in the given DataFrame. 
#-------------------------------------------------------------------------------
def search_company_by_name(df, query):
    """
    Args:
        df (pd.DataFrame): The DataFrame containing company data.
        query (str): The company name to search for.

    Returns:
        pd.DataFrame: The DataFrame containing the search results.
    """
    result = df[df['Name'].str.contains(query, case=False, na=False)]
    return result[['Name', 'Symbol']]


#-------------------------------------------------------------------------------
# The main function that runs the Streamlit application.
#-------------------------------------------------------------------------------
def main():
    st.title("🔎 Company Search")

    # Load data from the CSV file
    df = pd.read_csv("nasdaq_screener.csv")

    # Input box to enter the company name to search
    search_query = st.text_input("Enter the company name to search:")

    if search_query:
        # Search and display results
        search_results = search_company_by_name(df, search_query)
        if not search_results.empty:
            st.header("Search Results:")
            st.dataframe(search_results, height=len(search_results) * 50)
        else:
            st.warning("No matching companies found.")

#-------------------------------------------------------------------------------
# Driver
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

