import requests
from bs4 import BeautifulSoup
import csv
import time

# Store all books data
all_books_data = []

# Loop through pages (change 3 → 50 later)
for page_num in range(1, 3):

    url = f"http://books.toscrape.com/catalogue/page-{page_num}.html"
    print(f"Scraping page {page_num}: {url}")

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Page {page_num} not found. Stopping.")
        break

    soup = BeautifulSoup(response.content, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip("£")
        availability = book.find("p", class_="instock availability").text.strip()
        rating = book.p["class"][1]

        all_books_data.append([title, price, availability, rating])

    print(f"Page {page_num} scraped. Waiting 1 second...")
    time.sleep(1)

# Save to CSV
with open("all_books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Header
    writer.writerow(["Title", "Price", "Availability", "Rating"])
    
    # All rows
    writer.writerows(all_books_data)

print(f"\n✅ Scraping complete! Found {len(all_books_data)} books.")