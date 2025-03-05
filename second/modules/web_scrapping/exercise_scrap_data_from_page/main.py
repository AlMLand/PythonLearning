import logging

from selenium_engine import SeleniumEngine

logging.basicConfig(level=logging.INFO)

engine = SeleniumEngine()
engine.go_to("https://toscrape.com/")
engine.click_by_class_name("col-md-6")

engine.close()
