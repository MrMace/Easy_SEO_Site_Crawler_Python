import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the website
    response = requests.get(url)
    
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the page title
    page_title = soup.title.string if soup.title else 'No title'
    
    # Extract the meta description
    meta_description = soup.find('meta', attrs={'name': 'description'})
    meta_description = meta_description['content'] if meta_description else 'No description'
    
    # Extract all headers (h1, h2, h3)
    headers = [header.text.strip() for header in soup.find_all(['h1', 'h2', 'h3'])]
    
    # Return the scraped data
    return {
        'title': page_title,
        'description': meta_description,
        'headers': headers
    }

# Example usage
url = 'https://www.example.com'  # Replace with the target website URL
scraped_data = scrape_website(url)
print('Title:', scraped_data['title'])
print('Description:', scraped_data['description'])
print('Headers:', scraped_data['headers'])

