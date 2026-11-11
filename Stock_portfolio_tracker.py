import csv
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 200
}
for stock, price in stock_prices.items():
    print(f"{stock} :₹ {price}")
portfolio = []
num = int(input("Enter Number of Stock :"))
for i in range(num):
    stock_name = input("Enter Stock Name :").strip().upper()
    if stock_name not in stock_prices :
        print(f"Stock Not Available !!")
        continue
    
        
    try:
        stock_qty = int(input("Enter Stock Quantity :"))
        if stock_qty <= 0 :
            print("Stock Quantity Must be Greater than 0!\n")
            continue
    except ValueError :
        print("Invalid Number Entered !!")
        continue
    price = stock_prices[stock_name]
    investment = price * stock_qty
    portfolio.append({
        "stock_name": stock_name,
        "stock_qty":stock_qty,
        "price" :price,
        "investment":investment
    })
    print(f"{stock_name} * {stock_qty} = ₹{investment}\n")

header = ["stock_name","stock_qty","price","investment"]
filename = "portfolio.csv"
with open(filename, mode = "w",encoding= "utf-8") as file:
    writer = csv.DictWriter(file, fieldnames= header)
    writer.writeheader()
    writer.writerows(portfolio)
print(f"data SuccessFully Saved as {filename}\n")
