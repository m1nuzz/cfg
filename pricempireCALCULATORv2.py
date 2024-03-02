import webbrowser

def generate_links(base_url, skin_cost, num_variants):
    links = []

    # Generate links with different variants of skin cost
    for i in range(2, num_variants + 1):
        modified_url = base_url.replace('COST', str(skin_cost / i)) + f"&variant={i}"
        links.append((modified_url, i))

    return links

def main():
    try:
        # Request skin cost and number of variants from the user
        skin_cost = float(input("Enter the skin cost: "))
        num_variants = int(input("Enter the number of variants: "))
    except ValueError:
        print("Please enter valid numeric values.")
        return

    # Base URL for price comparison
    base_url = "https://pricempire.com/comparison?priceFrom=0.3&priceTo=COST&compareToFee=&sort=profit:DESC&steamVolume=15&priceDays=120&qtyFrom=1&qtyTo=10&minRoi=0&maxRoi=1000&liquidity=50"

    # Generate a list of links with variants
    links_with_variants = generate_links(base_url, skin_cost, num_variants)

    # Open the links in the browser and print the associated variant
    for link, variant in links_with_variants:
        print(f"Opening variant {variant}: {link}")
        webbrowser.open(link)

if __name__ == "__main__":
    main()
