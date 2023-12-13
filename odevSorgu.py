import requests
url = "https://api.screenshotlayer.com/api/capture"
response = requests.get(url)
data = response.json()
print(data)