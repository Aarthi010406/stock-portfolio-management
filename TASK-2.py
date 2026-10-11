STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def get_portfolio():
    """Ask the user for stock names and quantities until they type 'done'."""
    portfolio = {}  # stock name -> quantity

    print("Available stocks:")
    for name, price in STOCK_PRICES.items():
        print(f"  {name}: ${price}")
    print("\nEnter a stock name and quantity. Type 'done' when finished.\n")

    while True:
        name = input("Stock name: ").upper().strip()

        if name == "DONE":
            break
        if name not in STOCK_PRICES:
            print("Unknown stock. Please choose from the list above.")
            continue

        qty_text = input(f"Quantity of {name}: ").strip()
        if not qty_text.isdigit() or int(qty_text) <= 0:
            print("Please enter a whole number greater than 0.")
            continue

        # Add to any quantity already entered for this stock
        portfolio[name] = portfolio.get(name, 0) + int(qty_text)

    return portfolio


def build_report(portfolio):
    """Return the report as a list of text lines, plus the total value."""
    lines = [f"{'Stock':<8}{'Qty':>6}{'Price':>10}{'Value':>12}"]
    lines.append("-" * 36)

    total = 0
    for name, qty in portfolio.items():
        price = STOCK_PRICES[name]
        value = price * qty
        total += value
        lines.append(f"{name:<8}{qty:>6}{price:>10}{value:>12}")

    lines.append("-" * 36)
    lines.append(f"Total investment value: ${total}")
    return lines


def main():
    print("=== STOCK PORTFOLIO TRACKER ===\n")
    portfolio = get_portfolio()

    if not portfolio:
        print("\nNo stocks entered.")
        return

    report = build_report(portfolio)
    print()
    for line in report:
        print(line)

    save = input("\nSave this report to a file? (y/n): ").lower().strip()
    if save == "y":
        with open("portfolio.txt", "w") as file:
            file.write("\n".join(report) + "\n")
        print("Saved to portfolio.txt")


if __name__ == "__main__":
    main()