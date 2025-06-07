# Liu-scraper

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
