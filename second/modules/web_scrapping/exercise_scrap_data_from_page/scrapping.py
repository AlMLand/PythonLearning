import re

import requests
from bs4 import BeautifulSoup


def get_book_titles(url: str):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')

    book_titles = []
    products = soup.select(".product_pod")
    for product in products:
        if product.select(".star-rating.Two"):
            title = product.select("h3 a")[0]["title"]
            book_titles.append(title)

    return book_titles


def get_max_page_size(url: str):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    pages = soup.select(".current")[0].get_text()
    max_pages = _extract_last_number(pages)

    if max_pages is None:
        raise ValueError("Could not extract the last number from the page")

    return max_pages


def _extract_last_number(text: str) -> int | None:
    match = re.search(r'of (\d+)', text)
    if match:
        return int(match.group(1))

    return None
