# -*- coding: utf-8 -*-
"""Scanlon_Download_Historical_Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HanMR63MW4YZzwTI5xLPrvkOfFRhS9km
"""

import yfinance as yf

# Tickers of my choosing (I am actually invested in these)
tickers = ['SBUX', 'AAPL', 'GOOG']

# Download historical data for each of the aforementioned company
data = {}
for ticker in tickers:
    #The more historical data the better, so I used the last 14 years
    data[ticker] = yf.download(ticker, start="2010-01-01", end="2024-02-23")

