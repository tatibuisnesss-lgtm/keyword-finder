from playwright.sync_api import sync_playwright
import time
import random

KEYWORD = "revenge"
found = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
    )

    page = context.new_page()

    for i in range(1, 101):
        url = f"https://hqporner.com/hdporn/{i}"

        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(3000)

            text = page.locator("body").inner_text().lower()

            if KEYWORD in text:
                print(f"Found on page {i}")
                found.append(i)

        except Exception as e:
            print(f"Page {i}: {e}")

        time.sleep(random.uniform(2, 5))

    browser.close()

print(found)