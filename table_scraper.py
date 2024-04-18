import streamlit as st
import pandas as pd

# Function to scrape tables from a URL
@st.cache_resource
def scrape_tables(url):
    tables = pd.read_html(url)
    return tables

# Streamlit app
def main():
    st.title("Table Scraper App")

    url = st.text_input("Enter URL")
    if url:
        tables = scrape_tables(url)
        for i, table in enumerate(tables):
            st.write(f"Table {i+1}")
            st.write(table)

if __name__ == "__main__":
    main()