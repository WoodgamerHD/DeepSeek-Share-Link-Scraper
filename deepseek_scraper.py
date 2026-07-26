import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def get_all_deepseek_share_links(output_file="deepseek_share_links.txt", max_pages=10):
    """
    Scrape all DeepSeek share links from Google search results, page by page.

    Args:
        output_file (str): File to save the links.
        max_pages (int): Maximum number of result pages to fetch (Google caps at ~10).
    """
    # Set up the Chrome driver (optional: add headless mode or options)
    options = webdriver.ChromeOptions()
    # Uncomment the next line to run in headless mode (no browser window)
    # options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    base_url = "https://www.google.com/search?q=site:chat.deepseek.com/share/&filter=0"
    current_url = base_url
    all_links = set()
    page_num = 1

    try:
        while page_num <= max_pages:
            print(f"\n🔍 Fetching page {page_num}...")
            driver.get(current_url)

            # Wait for the search results to appear
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div#search"))
                )
            except TimeoutException:
                print("⚠️  Timeout waiting for results. Maybe Google blocked the request.")
                break

            # Scroll a bit to ensure all lazy-loaded items appear
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            # Extract all links with the target domain
            link_elements = driver.find_elements(By.CSS_SELECTOR, "a[href*='chat.deepseek.com/share/']")
            for el in link_elements:
                href = el.get_attribute("href")
                if href and href.startswith("https://chat.deepseek.com/share/"):
                    all_links.add(href)

            print(f"✅ Found {len(link_elements)} links on this page. Total so far: {len(all_links)}")

            # Try to find the "Next" button
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, "a#pnnext")
                next_url = next_button.get_attribute("href")
                if not next_url:
                    print("ℹ️  'Next' button found but no URL. Stopping.")
                    break
                current_url = next_url
                page_num += 1
            except NoSuchElementException:
                print("ℹ️  No more 'Next' button. Reached the last page.")
                break

    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        driver.quit()

    # Save results
    if all_links:
        with open(output_file, "w", encoding="utf-8") as f:
            for link in sorted(all_links):
                f.write(link + "\n")
        print(f"\n📁 Exported {len(all_links)} unique share links to {output_file}")
    else:
        print("❌ No links found.")

if __name__ == "__main__":
    get_all_deepseek_share_links(max_pages=10)   # adjust max_pages if needed
