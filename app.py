import streamlit as st
import requests
from bs4 import BeautifulSoup


def scrape_website_content(url, target_class):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find elements with the specified class
        elements = soup.find_all(class_=target_class)

        # Extract and return the content
        return [element.get_text() for element in elements]
    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"


def main():
    # Streamlit app
    st.title("Web Scraping App")

    # First website
    st.header("Government Scheme 1")
    col_class_1 = "col-md-9 col-sm-8"
    content_1 = scrape_website_content(
        "https://nbcfdc.gov.in/pm-daksh/en", col_class_1)
    for content in content_1:
        st.write(content)

    # Second website
    st.header("Government Scheme 2")
    target_class_2 = "entry-content"
    content_2 = scrape_website_content(
        "https://tweetindia.org/gurukul-for-trans-excellence/", target_class_2)
    for content in content_2:
        st.write(content)


if __name__ == "__main__":
    main()
