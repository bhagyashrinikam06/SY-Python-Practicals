def price_engine(asset_costs):
    # Sort prices from highest to lowest
    sorted_costs = sorted(asset_costs, reverse=True)

    # Get the top three prices
    top_three = sorted_costs[:3]

    print("Top 3 Priciest Entries:")
    for i, price in enumerate(top_three, start=1):
        print(f"{i}. ₹{price:.2f}")


# Example list of asset costs
asset_costs = [12500.75, 45000.50, 3200.25, 78500.00, 25000.80, 99000.99]

# Run the price engine
price_engine(asset_costs)
