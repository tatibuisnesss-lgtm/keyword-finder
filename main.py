from playwright.sync_api import sync_playwright
import time
import random

KEYWORD = "revenge"
found = []

start_time = time.time()

with sync_playwright() as p:
    print("Launching browser...", flush=True)

    browser = p.chromium.launch(headless=True)

    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
    )

    page = context.new_page()

    print("Starting scan...\n", flush=True)

    for i in range(101, 200):
        url = f"https://hqporner.com/hdporn/{i}"

        elapsed = int(time.time() - start_time)

        print(
            f"[{i:03}/100] ({elapsed}s) Checking {url}",
            flush=True
        )

        try:
            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=60000
            )

            page.wait_for_timeout(3000)

            text = page.locator("body").inner_text().lower()

            if KEYWORD in text:
                found.append(i)
                print(
                    f"    ✅ FOUND on page {i} | Total found: {len(found)}",
                    flush=True
                )
            else:
                print("    ❌ Not found", flush=True)

        except Exception as e:
            print(f"    ⚠ ERROR: {e}", flush=True)

        time.sleep(random.uniform(2, 5))

    browser.close()

total = round(time.time() - start_time, 2)

print("\n==============================", flush=True)
print("Finished!", flush=True)
print(f"Keyword: {KEYWORD}", flush=True)
print(f"Pages scanned: 100", flush=True)
print(f"Matches: {len(found)}", flush=True)
print(f"Found on: {found}", flush=True)
print(f"Total time: {total} seconds", flush=True)
print("==============================", flush=True)
