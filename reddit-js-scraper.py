from crawlbase import CrawlingAPI

api = CrawlingAPI({ 'token': 'CRWALBASE JS TOKEN HERE' })

response = api.get('https://www.reddit.com/r/wealthfront/', { 'autoparse': 'true' })

print(response['body'])
print(response['status_code'])