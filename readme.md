# Financial Multiples Analysis Scraper

## Purpose

In the world of investment banking and financial analysis, assessing a company's value often involves analyzing financial multiples, such as EV/EBITDA and P/E ratios. Traditionally, this process is labor-intensive, requiring analysts to manually search for and gather financial data from various sources, which can be particularly cumbersome with a large list of companies.

This project automates this process by scraping financial metrics from the web. By inputting a list of company stock tickers, the code fetches and displays relevant financial data, streamlining the analysis and significantly reducing the time and effort involved.

## How It Works

The script takes a list of company stock tickers and scrapes financial metrics from [StockAnalysis.com](https://stockanalysis.com). It then formats and displays the data for each company, making it easier to perform financial multiples analysis without manual data collection.

### Website Selection: StockAnalysis.com

- **Static Website:** StockAnalysis.com is a static website with financial data contained within parseable HTML table tags (`<tr>` and `<td>`). This structure allows for straightforward data extraction.
  
- **Regulation Compliance:** According to the site's `robots.txt` file, scraping is allowed, provided that disallowed bots (e.g., dotbot, BLEXBot, mj12bot) are not used.

## How to Run

1. **Clone the Repository**

   To get started, first clone the repository to your local machine:

   ```bash
   git clone https://github.com/moeez-tariq/stockAnalysisScrape.git
   cd stockAnalysisScrape
   ```

2. **Install Dependencies**

   Create a virtual environment and install the required packages:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the Script**

   Change the 'companyTickers' list in main.py to add the companies you want. Run the script with the desired list of stock tickers:

   ```bash
   python main.py
   ```
   The script will then scrape the financial data and display it for each company.

## Team Members
1. Allan Zhan
2. Allen Feng
3. Muhammad Moeez Tariq