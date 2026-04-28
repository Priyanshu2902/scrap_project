from bs4 import BeautifulSoup
import requests

url = "https://example.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

data = []

for link in links:
    text = link.text.strip()
    href = link.get("href")  # safer than link["href"]

    data.append({
        "text": text,
        "href": href
    })

print(data)