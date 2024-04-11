# Scraping State Election Data

## Overview

This repo contains materials for a training I lead on different strategies for scraping data. It contains updated examples based on the methods discussed in [this blog post](https://www.emilyriederer.com/post/states-scraping-automation/).

Different ways of displaying data on the web require different execution strategies. This repo demonstrates the following:

- File download with `urllib.requests` (NC)
- Webscraping server-side rendered (PHP) data with `BeautifulSoup` (MI)
- Webscraping client-side rendered (JS) data with `playwright` (VA)
- Headless browsing to download file with `playwright` (TX)
- Headless browsing, RPA (screenshot), and OCR from a dashboard (RI)

These methods increase in complexity as easier methods fail:

- When data exists in a premade file, we can simply download it
- When data exists as a table within a website, we can scrape if it is pre-rendered
- When we need to trigger rendering or navigate a UI, we may need to use headless browsing to accomplish analogous tasks
- When data is "trapped" in an unnavigable GUI (e.g. embedded dashboard), we may need to use OCR

Examples are not intended to demonstrate best practices for scalable pipelines but rather to provide accessible code for explaining different scraping methods and when each is most appropriate. 

## Set-Up

For Windows:

```
git clone https://github.com/emilyriederer/data-scraping-states.git
cd data-scraping-states
python -m venv .venv 
.venv\Scripts\activate
pip install requirements.txt
python -m pip install -r requirements.txt
```

For `05-rpa-ocr-ri.py`, you will also need to install [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki).