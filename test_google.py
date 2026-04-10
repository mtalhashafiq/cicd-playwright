import os
from playwright.sync_api import sync_playwright
import time

def test_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto("https://example.com")
            assert "Example" in page.title()

        except Exception:
            page.screenshot(path="failure.png")  # 🔥 screenshot on fail
            raise

        finally:
            time.sleep(5)  # 💤 wait a bit before closing
            browser.close()