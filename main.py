import requests

url = "https://example.com"

response = requests.get(url)

print("Status Code:", response.status_code)
print("First 200 chars:\n", response.text[:200])