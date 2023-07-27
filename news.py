import streamlit as st
from bs4 import BeautifulSoup as BS
import requests as req

url = "https://www.businesstoday.in/latest/economy"

#-------------------------------------------------------------------------------
# Scrapes headlines and article links from a webpage.
#-------------------------------------------------------------------------------
def scraping(): 
    """
    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        Tuple[List[str], List[str]]: A tuple containing a list of headlines and a list of article links.
    """
    # Make a GET request to the webpage
    webpage = req.get(url)

    # Create a BeautifulSoup object to parse the webpage content
    trav = BS(webpage.content, "html.parser")

    # Initialize empty lists to store the headlines and article links
    headlines = []
    article_links = []
    M = 1

    # Iterate over all 'a' tags in the parsed content
    for link in trav.find_all('a'):
        # Check if the link text is a NavigableString and has length > 35
        if (
            str(type(link.string)) == "<class 'bs4.element.NavigableString'>"
            and len(link.string.strip()) > 35
        ):
            # Extract the headline and add it to the headlines list
            headline = link.string.strip()
            headlines.append(headline)

            # Extract the article link and add it to the article links list
            article_link = link['href'] if link['href'].startswith('http') else 'https://www.businesstoday.in' + link['href']
            article_links.append(article_link)
            M += 1

    return headlines, article_links

#-------------------------------------------------------------------------------
# This function displays the latest economy news headlines fetched from 
# a specific source.
#-------------------------------------------------------------------------------

def main():
    # Set the title of the page
    st.title("💸 Financial News")

    # Fetch and display financial news headlines related to the Economy category with a length greater than 35 characters
    headlines, article_links = scraping()

    # Display the header for the latest economy news headlines
    st.header("Latest Economy News Headlines:")
    # Display the source of the news headlines
    st.markdown('_Source: Business Today_')

    # Display each headline with its corresponding link
    for i, (headline, link) in enumerate(zip(headlines, article_links), 1):
        st.markdown(f"{i}. [{headline}]({link})")

#-------------------------------------------------------------------------------
# Driver
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
