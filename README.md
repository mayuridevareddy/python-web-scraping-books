# python-web-scraping-books

> Extracts structured book data from paginated websites and exports clean CSV files.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4-green?style=flat-square)
![Requests](https://img.shields.io/badge/Requests-HTTP-orange?style=flat-square)
![CSV](https://img.shields.io/badge/Output-CSV-teal?style=flat-square)

---

## Tech stack

| Library | Role |
|---|---|
| `requests` | Sends HTTP requests to target pages |
| `beautifulsoup4` | Parses and navigates HTML content |
| `csv` (stdlib) | Writes extracted data to file |

---

## Features

- Scrapes **Title, Price, Availability, and Rating** for each book
- Handles **multi-page pagination** automatically
- Exports a clean, analysis-ready **CSV file**
- Beginner-friendly code structure, easy to extend

---

## Project structure
```
python-web-scraping-books/
├── scraper.py       # main scraping script
├── all_books.csv    # extracted dataset
└── README.md        # documentation
```

---

## How it works

1. Sends an HTTP GET request to the target website
2. Parses the HTML response with BeautifulSoup
3. Extracts Title, Price, Availability, and Rating fields
4. Follows pagination links to scrape all pages
5. Writes the collected data into `all_books.csv`

---

## Setup & usage

Install dependencies:
```bash
pip install requests beautifulsoup4
```

Run the scraper:
```bash
python scraper.py
```

---

## Sample output

| Title | Price | Availability | Rating |
|---|---|---|---|
| A Light in the Attic | £51.77 | In stock | Three |
| Tipping the Velvet | £53.74 | In stock | One |
| Soumission | £50.10 | In stock | One |
