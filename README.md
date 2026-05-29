# 🏏 ICC Men's T20I Team Rankings — Web Scraping Project

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.12-green?style=for-the-badge&logo=beautifulsoup&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2.x-blue?style=for-the-badge)

## 📌 Project Overview

This project scrapes the **ICC Men's T20I Team Rankings** directly from Wikipedia using Python. It extracts the live rankings table, cleans the data, builds a structured Pandas DataFrame, and exports it to CSV — all with just a few lines of code.

---

## 🎯 Objectives

- Scrape live HTML data from a Wikipedia rankings table
- Parse and clean raw HTML using BeautifulSoup
- Structure the data into a clean Pandas DataFrame
- Export the final dataset to CSV for further analysis

---

## 🛠️ Tools & Libraries

| Tool | Purpose |
|---|---|
| `requests` | Fetch the Wikipedia webpage |
| `BeautifulSoup` | Parse and extract HTML content |
| `pandas` | Structure and manipulate data |
| `lxml` | HTML parser backend |

---

## 📂 Project Structure

```
icc-t20-rankings/
│
├── icc_t20_rankings.py     # Main scraping script
├── icc_t20_rankings.csv    # Output dataset (generated on run)
└── README.md               # Project documentation
```

---

## ▶️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/BhadurAli/icc-t20-rankings.git
cd icc-t20-rankings
```

**2. Install dependencies**
```bash
pip install requests pandas beautifulsoup4 lxml
```

**3. Run the script**
```bash
python icc_t20_rankings.py
```

**4. Output**

The script will print the top 10 teams and save a `icc_t20_rankings.csv` file in the same directory.

---

## 📊 Sample Output

| Rank | Team | Matches | Points | Rating |
|---|---|---|---|---|
| 1 | India | 56 | 7952 | 142 |
| 2 | England | 47 | 6441 | 137 |
| 3 | Australia | 52 | 6891 | 133 |
| ... | ... | ... | ... | ... |

---

## 💡 Key Learnings

- How to send HTTP requests with custom User-Agent headers
- Parsing nested HTML tables with BeautifulSoup
- Cleaning scraped data (removing footer rows, stripping whitespace)
- Structuring raw scraped data into a Pandas DataFrame

---

## 🔗 Data Source

[ICC Men's T20I Team Rankings — Wikipedia](https://en.wikipedia.org/wiki/ICC_Men%27s_T20I_Team_Rankings)

---

## 👨‍💻 Author

**Bhadur Ali** — Data Analyst & Junior Data Scientist  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/bhadur-ali)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:alikhansalar5@gmail.com)
