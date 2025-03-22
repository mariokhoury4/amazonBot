from bs4 import BeautifulSoup

def extract_product_title(soup: BeautifulSoup) -> str:
    title_element = soup.find(id="productTitle")
    if not title_element:
        raise ValueError("Product title not found.")
    return title_element.get_text().strip()

def extract_price(soup: BeautifulSoup) -> float:
    price_element = soup.find(id="priceblock_ourprice") or soup.find(id="priceblock_dealprice")
    if price_element:
        price_text = price_element.get_text().strip()
    else:
        whole = soup.find("span", class_="a-price-whole")
        fraction = soup.find("span", class_="a-price-fraction")
        if whole:
            whole_text = whole.get_text().strip().replace(",", "").replace(".", "")
            fraction_text = fraction.get_text().strip().replace(",", "").replace(".", "") if fraction else "00"
            price_text = f"{whole_text}.{fraction_text}"
        else:
            raise ValueError("Price not found.")
    return float(price_text.replace("$", "").replace(",", ""))
