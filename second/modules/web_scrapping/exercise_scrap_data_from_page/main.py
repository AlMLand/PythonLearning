import logging

from scrapping import get_book_titles, get_max_page_size
from selenium_engine import SeleniumEngine

logging.basicConfig(level=logging.INFO)

engine = SeleniumEngine()
engine.go_to("https://toscrape.com/")
engine.click_by_class_name("col-md-6")

max_page_size = get_max_page_size(engine.get_current_url())

book_titles = []
for page_number in range(max_page_size):
    book_titles.extend(get_book_titles(engine.get_current_url()))
    engine.click_by_class_name("next")

print(f"Found {len(book_titles)} books")
print(book_titles)
engine.close()
