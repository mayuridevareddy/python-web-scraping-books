# 📚 Python Web Scraping Project

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Data-CSV-orange?style=for-the-badge">
</p>

---

## 🚀 Project Overview

This project is a **Python-based web scraper** that extracts structured book data from a website and stores it into a CSV file for analysis.

---

## 🔧 Tech Stack

- 🐍 Python  
- 🌐 Requests  
- 🍲 BeautifulSoup  
- 📄 CSV  

---

## ✨ Features

✔ Scrapes book details (Title, Price, Availability, Rating)  
✔ Handles **multi-page scraping (pagination)**  
✔ Stores clean structured data into CSV  
✔ Beginner-friendly and scalable  

---

## 📂 Project Structure

📁 python-web-scraping-books

│
├── scraper.py # Main scraping script
├── all_books.csv # Extracted dataset
└── README.md # Project documentation

---

## ⚙️ How It Works

1. Sends request to website  
2. Parses HTML using BeautifulSoup  
3. Extracts required data fields  
4. Loops through multiple pages  
5. Saves data into CSV file  

---

## ▶️ How to Run

```bash
pip install requests beautifulsoup4
python scraper.py

| Title        | Price | Availability | Rating |
| ------------ | ----- | ------------ | ------ |
| Example Book | 51.77 | In stock     | Three  |
