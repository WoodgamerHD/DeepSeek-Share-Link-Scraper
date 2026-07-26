# DeepSeek Share Link Scraper

A Python script that automatically extracts publicly shared **DeepSeek conversation links** (`https://chat.deepseek.com/share/*`) from Google Search results using Selenium.

The scraper navigates through Google search result pages, collects all matching share links, removes duplicates, and exports them to a text file.

> **Disclaimer:** This tool is intended for educational and research purposes only. Always comply with Google's Terms of Service and applicable laws when scraping websites.

---

## ✨ Features

* 🔍 Scrapes Google search results for DeepSeek share links
* 📄 Automatically navigates through multiple pages
* 🔄 Removes duplicate URLs
* 💾 Exports all unique links to a text file
* ⚙️ Easily configurable page limit and output filename
* 🖥️ Optional headless mode for running without opening Chrome

---

## 📋 Requirements

* Python **3.6+**
* Google Chrome
* ChromeDriver matching your Chrome version
* Selenium

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/WoodgamerHD/DeepSeek-Share-Link-Scraper.git
cd DeepSeek-Share-Link-Scraper
```

Install the required dependency:

```bash
pip install selenium
```

Download **ChromeDriver** matching your installed Chrome version and either:

* Add it to your system **PATH**, or
* Specify its location in the script.

---

## 🚀 Usage

Run the scraper:

```bash
python deepseek_scraper.py
```

The script will:

1. Open Google Search.
2. Search for publicly shared DeepSeek conversations.
3. Visit each results page.
4. Collect all matching `https://chat.deepseek.com/share/*` links.
5. Remove duplicates.
6. Save the results to a text file.

---

## ⚙️ Configuration

You can customize the following variables inside the script:

| Setting       | Description                                     | Default                    |
| ------------- | ----------------------------------------------- | -------------------------- |
| `max_pages`   | Maximum number of Google result pages to scrape | `10`                       |
| `output_file` | Output filename                                 | `deepseek_share_links.txt` |

### Headless Mode

To run Chrome without opening a browser window, uncomment the headless option:

```python
options.add_argument("--headless=new")
```

---

## 📄 Example Output

Console output:

```text
🔍 Fetching page 1...
✅ Found 8 links on this page. Total so far: 8

🔍 Fetching page 2...
✅ Found 10 links on this page. Total so far: 18

...

ℹ️ No more 'Next' button. Reached the last page.

📁 Exported 89 unique share links to deepseek_share_links.txt
```

Example output file:

```text
https://chat.deepseek.com/share/abc123-def456-789
https://chat.deepseek.com/share/xyz789-uvw456
https://chat.deepseek.com/share/123456-abcdef
```

---

## 📁 Output

All discovered links are saved to:

```text
deepseek_share_links.txt
```

Each URL is written on its own line.

---

## ⚠️ Important Notes

### Google Rate Limits

Google may display CAPTCHAs or temporarily block automated requests after multiple searches. Since this project uses Selenium to control a real browser, it behaves more like a human user than traditional HTTP scraping, but rate limits can still occur.

### Search Result Limits

Google typically returns a maximum of around **100 organic search results**, meaning you'll usually reach the end after approximately **10 pages**.

### Educational Use

This project is provided for educational, research, and personal use only. Users are responsible for ensuring they comply with Google's Terms of Service and any applicable laws.

---

## 💡 Alternative Approach

For larger or more reliable data collection, consider using the **Google Custom Search JSON API**.

Benefits include:

* No browser automation
* Structured JSON responses
* Higher reliability
* Free tier (100 searches/day)

---

## 🤝 Contributing

Pull requests, feature suggestions, and bug reports are welcome.

If you have ideas for improvements, feel free to open an issue or submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.
