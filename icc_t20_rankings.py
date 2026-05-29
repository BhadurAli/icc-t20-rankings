# ============================================================
# ICC Men's T20I Team Rankings - Web Scraping Project
# Author: Bhadur Ali
# Description: Extracts ICC T20I team rankings from Wikipedia
# Tools: Python, BeautifulSoup, Requests, Pandas
# ============================================================

import requests
import pandas as pd
from bs4 import BeautifulSoup

# ── 1. Fetch the Wikipedia page ──────────────────────────────
url = "https://en.wikipedia.org/wiki/ICC_Men%27s_T20I_Team_Rankings"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

web = requests.get(url, headers=headers)
print(f"Status Code: {web.status_code}")

# ── 2. Parse HTML with BeautifulSoup ─────────────────────────
soup = BeautifulSoup(web.content, "lxml")

# ── 3. Extract the rankings table ────────────────────────────
table = soup.find_all("table")[1]

# Extract column headers
title = table.find_all("th")
column_headers = [i.text.strip() for i in title]

# Remove the footer/source row that gets picked up as a header
column_headers = [h for h in column_headers if not h.startswith("Source:")]

print(f"Columns found: {column_headers}")
print(f"Total columns: {len(column_headers)}")

# ── 4. Extract all data rows ──────────────────────────────────
column_row = table.find_all("tr")

rows = []
for row in column_row[1:]:
    data = row.find_all("td")
    rows.append([i.text.strip() for i in data])

# ── 5. Build the DataFrame ────────────────────────────────────
df = pd.DataFrame(rows, columns=column_headers)

# Drop the last footer row
df.drop(index=98, inplace=True)

# ── 6. Preview the data ───────────────────────────────────────
print("\n── ICC T20I Rankings ──")
print(df.head(10))
print(f"\nTotal teams: {len(df)}")

# ── 7. Export to CSV ──────────────────────────────────────────
df.to_csv("icc_t20_rankings.csv", index=False)
print("\n✅ Data saved to icc_t20_rankings.csv")
