# Import the CrawlingAPI from the crawlbase module
from crawlbase import CrawlingAPI

# Set your Crawlbase token
crawlbase_token = 'CRAWLBASE TOKEN'

# Define the URL of the Reddit page to scrape
reddit_page_url = 'https://www.reddit.com/t/technology/'

# Set options for the Crawling API, enabling the autoparse feature
options = {
    'autoparse': 'true',
}

# Create an instance of the CrawlingAPI with your token
api = CrawlingAPI({'token': crawlbase_token})
try:
    # Send a GET request to crawl the specified URL with the provided options
    response = api.get(reddit_page_url, options=options)
    # Check if the response status code is 200 (OK)
    if response.get('statusCode', 0) == 200:
        # Parse the JSON response and print it
        response_body_json = response.get('body', {})
        print(response_body_json)
    else:
        # Print an error message if the request fails
        print(f"Request failed with status code: {response.get('statusCode', 0)}")
except Exception as e:
    # Handle any exceptions or errors that may occur during the API request
    print(f"API request error: {str(e)}")