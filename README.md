# 🐍 python-web-scraping-books

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4-4CAF50?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-FF6B35?style=for-the-badge&logo=python&logoColor=white)
![CSV](https://img.shields.io/badge/Output-CSV-9B59B6?style=for-the-badge&logo=files&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**Scrapes structured book data from paginated websites and exports clean CSV files.**

</div>

---

## 🔷 Tech Stack

| 📦 Library | 🎯 Role |
|:---|:---|
| `requests` | Sends HTTP requests to target pages |
| `beautifulsoup4` | Parses and navigates HTML content |
| `csv` *(stdlib)* | Writes extracted data to file |

---

## 🚀 Features

| ✅ Feature | 📝 Description |
|:---|:---|
| 📚 Book details | Extracts Title, Price, Availability and Rating |
| 🔄 Pagination | Automatically loops through all pages |
| 💾 CSV export | Saves clean, analysis-ready data |
| 🧩 Scalable | Beginner-friendly and easy to extend |

---

## 📂 Project Structure
```
📁 python-web-scraping-books/
│
├── 🐍 scraper.py       ← main scraping script
├── 📄 all_books.csv    ← extracted dataset
└── 📘 README.md        ← documentation
```

---

## ⚙️ How It Works
```
🌐 Send HTTP request
        ↓
🍲 Parse HTML with BeautifulSoup
        ↓
🔍 Extract → Title | Price | Availability | Rating
        ↓
📑 Follow pagination links
        ↓
💾 Save to all_books.csv
```

---

## ▶️ Setup & Usage

**1. Install dependencies**
```bash
pip install requests beautifulsoup4
```

**2. Run the scraper**
```bash
python scraper.py
```

---

## 📊 Sample Output

| 📖 Title | 💰 Price | 🏷️ Availability | ⭐ Rating |
|:---|:---:|:---:|:---:|
| A Light in the Attic | £51.77 | ✅ In stock | ⭐⭐⭐ Three |
| Tipping the Velvet | £53.74 | ✅ In stock | ⭐ One |
| Soumission | £50.10 | ✅ In stock | ⭐ One |

---

<div align="center">

Made with ❤️ using Python & BeautifulSoup

![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square&logo=python)

</div>
