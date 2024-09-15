# import libraries
import requests
from bs4 import BeautifulSoup

# Function to display the scrapped financial data in a clean format
def displayTable(dataDict):
    # takes maximum length for both key and value for the max width of the columns
    maxKeyLength = max(len(key) for key in dataDict.keys())
    maxValueLength = max(len(value) for value in dataDict.values())

    rowFormat = "{:<" + str(maxKeyLength) + "} | {:>" + str(maxValueLength) + "}" # left and right align

    print(rowFormat.format("Ratio", "Value"))
    print("-" * maxKeyLength + " | " + "-" * maxValueLength)

    # print each pair in the dictionary (formatted)
    for key, value in dataDict.items():
        print(rowFormat.format(key, value))

# function to scrap the data from stockanalysis.com
def acquire_data(company_list):

    for companyTicker in company_list:

      #Establish connection to website server
      url = f'https://stockanalysis.com/stocks/{companyTicker}/financials/ratios/'
      response = requests.get(url)

      if response.status_code == 200:
          #Parse raw HTML code and extract financial metrics using BeautifulSoup
          soup = BeautifulSoup(response.text, 'html.parser')
          rows = soup.find_all('tr', class_='svelte-1dtewt4')
          valueDict = {}
          for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 2:
              key = columns[0].text.strip() # row specifiers
              value = columns[1].text.strip() # current value
              valueDict[key] = value
          #Display the acquired financial metrics by calling the formatting function
          print(f"Data for Company {companyTicker}")
          displayTable(valueDict)
          print("\n\n")
      else:
          print(f"Failed to retrieve the webpage for {companyTicker}. Enter valid company ticker.\n\n\n")

# Main feature code
companyTickers = ["NVDA","BAC","GOOG","MSFT"] # enter company tickers here
acquire_data(companyTickers)