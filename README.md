DeepSeek Share Link Scraper
A Python script that extracts all publicly shared DeepSeek conversation links (https://chat.deepseek.com/share/*) by scraping Google search results page by page.

Features
Page-by-page navigation – automatically clicks through Google's "Next" button until the last page.

Deduplication – stores only unique links.

Exports to a text file – each link on a new line.

Configurable – set the maximum number of pages to fetch.

Prerequisites
Python 3.6 or higher

Google Chrome browser

ChromeDriver matching your Chrome version (must be in your PATH)

Installation
Clone the repository:

bash
git clone https://github.com/WoodgamerHD/deepseek-share-scraper.git
cd deepseek-share-scraper
Install the required Python package:

bash
pip install selenium
Download ChromeDriver from the official site and place it in a directory included in your system PATH, or specify its location in the script.

Usage
Run the script:

bash
python deepseek_scraper.py
Configuration
Inside the script, you can adjust:

max_pages – maximum number of Google result pages to scrape (default: 10). Google typically caps at ~10 pages.

output_file – name of the output file (default: deepseek_share_links.txt).

To run in headless mode, uncomment the --headless option in the ChromeOptions.

Example Output
text
🔍 Fetching page 1...
✅ Found 8 links on this page. Total so far: 8
🔍 Fetching page 2...
✅ Found 10 links on this page. Total so far: 18
...
ℹ️  No more 'Next' button. Reached the last page.

📁 Exported 89 unique share links to deepseek_share_links.txt
The generated file contains URLs like:

text
https://chat.deepseek.com/share/abc123-def456-789...
https://chat.deepseek.com/share/xyz789-uvw456...
Important Notes
Google Blocks Automated Scraping – This script uses Selenium to simulate a real browser, but Google may still present CAPTCHAs or throttle your IP after a few pages. For large‑scale or reliable scraping, use the Google Custom Search API instead.

Result Limits – Even with pagination, Google usually returns at most ~100 organic results. The script will stop when it can't find a "Next" button.

Legal – Respect Google's Terms of Service and the robots.txt of any website you scrape. This tool is intended for educational and personal use only.

Alternatives
For a more robust solution, consider using the official Google Custom Search JSON API. It provides structured JSON results without browser automation and offers a free tier of 100 searches per day.

License
MIT
