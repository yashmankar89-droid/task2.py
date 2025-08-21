stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 300
}
portfolio = {}

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in database. Try again.")
        continue
    qty = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty

total_investment = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_investment += value
    print(f"{stock} - {qty} shares x ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value = ${total_investment}")

save = input("Do you want to save results to file? (yes/no): ").lower()
if save == "yes":

    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio:\n")
        for stock, qty in portfolio.items():
            value = qty * stock_prices[stock]
            file.write(f"{stock} - {qty} shares x ${stock_prices[stock]} = ${value}\n")
        file.write(f"\n Total Investment Value = ${total_investment}\n")
    print("Portfolio saved to portfolio.txt")
