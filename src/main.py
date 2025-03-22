import json
from price_checker import track_price

def main():
    with open("../products.json", "r") as file:
        products = json.load(file)

    for product in products:
        url = product["url"]
        target_price = product["target_price"]
        print(f"\n🔍 Checking product: {url}")
        track_price(url, target_price)

if __name__ == "__main__":
    main()
