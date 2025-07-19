from playwright.sync_api import sync_playwright
import os

def scrape_chapter(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        content = page.inner_text("body")
        os.makedirs("scraping/screenshots", exist_ok=True)
        page.screenshot(path="scraping/screenshots/chapter1.png", full_page=True)
        browser.close()
    return content, "scraping/screenshots/chapter1.png"
