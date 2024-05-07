import requests

# API URL that you want to request
api_url = "https://api.data.amsterdam.nl/v1/gebieden/"

# Send request
r = requests.get(url=api_url)

# If the API is secured with an API key, you can specify it as follows:
# r = requests.get(url=url, headers={"authorization": <YOUR_API_KEY>})

print(f"URL requested: {api_url}")
print(r.json())  # Convert the response of the API to JSON format
