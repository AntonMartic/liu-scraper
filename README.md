# Liu-scraper

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**Liu-scraper** is a lightweight web scraper for collecting program and course information from [Linköping University's study information website](https://studieinfo.liu.se/). It uses the [Web Scraper](https://webscraper.io/) Chrome extension to extract data and Python scripts to convert and process the scraped data into structured JSON format.

---

## 🚀 Features

- Scrapes course and program content from LiU’s study portal.
- Uses a customizable sitemap with the Web Scraper Chrome extension.
- Converts CSV output into JSON using Python.
- Includes extra scripts for specific CSV processing tasks.

---

## 🧰 Requirements

- [Web Scraper Chrome extension](https://chrome.google.com/webstore/detail/web-scraper/jnhgnonknehpejjnehehllkliplmbmhn)
- Python 3

### Python dependencies:
- `csv` (built-in)
- `json` (built-in)
- `collections.defaultdict` (built-in)
- `re` (built-in)
- `bs4` (BeautifulSoup):

Install BeautifulSoup using pip:

```bash
pip install beautifulsoup4
```

---

## 📁 Folder Structure

```bash
Liu-scraper/
├── sitemaps/
│   └── sitemap.txt / sitemap.js         # Web Scraper sitemap file
├── scripts/
│   ├── csvtojson-programs.py            # Converts CSV to JSON
│   └── miscellaneous/                   # Other processing scripts
├── jsons/
│   └── example.json                     # Sample JSON output
├── README.md
└── LICENSE
```

---

## 🔧 How to Use

### 1. Load the Sitemap in Web Scraper

- Open the Chrome extension Web Scraper.
- Import the sitemap from `sitemaps/sitemap.txt` or `sitemap.js`.
- Edit the `startUrl` in the sitemap to target the program or course you want to scrape.

### 2. Scrape the Website

- Start the scraping job in the Web Scraper tool.
- Once complete, download the resulting CSV file.

### 3. Convert CSV to JSON

- Place the CSV in the appropriate folder.
- Run the Python conversion script:

```bash
python scripts/csvtojson-programs.py
```
- The output JSON will be saved in the jsons/ folder.

### 4. Use the JSON Output

- The structured JSON file can be used in websites, applications, or for further data processing.

---

## 📌 Notes

- Designed for small-scale academic scraping projects.
- The miscellaneous folder contains helper scripts for refining or transforming specific CSV fields.
- Please use responsibly and respect the website’s terms of service.

---

## 🧑‍💻 Author

Created by Anton — a student project to streamline data extraction from LiU’s course information system.
