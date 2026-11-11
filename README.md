# 📈 Stock Portfolio Tracker using Python

A simple Python-based Stock Portfolio Tracker that calculates the total value of a user's stock investments using predefined stock prices and user-entered quantities.

## 📌 Project Overview

This project allows users to enter stock symbols and the number of shares they own.

The program checks the entered stock symbol against a predefined stock-price dictionary and calculates the investment value.

**Formula:**

```text
Investment Value = Stock Price × Quantity
```

The portfolio value is calculated using the values of the selected stocks.

## ✨ Features

- Predefined stock symbols and prices.
- User input for stock symbols.
- User input for stock quantities.
- Validates stock symbols against available entries.
- Calculates individual stock investment values.
- Displays the calculated portfolio value.

## 🛠️ Technologies Used

- Python 3
- Dictionaries
- Loops
- Conditional statements
- User input and output
- Basic arithmetic operations


## 💡 Example

Suppose the predefined stock price is:

```python
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 400
}
```

If the user enters:

```text
Stock Symbol: AAPL
Quantity: 5
```

Calculation:

```text
180 × 5 = 900
```

The investment value for AAPL is 900.

