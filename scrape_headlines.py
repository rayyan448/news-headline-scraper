import requests
from bs4 import BeautifulSoup

# Get the HTML
url = "https://www.npr.org/sections/news/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the news headlines

headlines = soup.find_all("h2", class_="title")

# Save to a list
headline_list = []
for headline in headlines:
    text = headline.get_text(strip=True)
    if text:
        headline_list.append(text)

# Write to file
with open("npr_headlines.txt", "w", encoding="utf-8") as f:
    for i, line in enumerate(headline_list, 1):
        f.write(f"{i}. {line}\n")

print("Headlines successfully scraped from NPR and saved to npr_headlines.txt")
