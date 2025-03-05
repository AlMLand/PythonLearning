import logging
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger(__name__)


class SeleniumEngine:
    def __init__(self):
        options = webdriver.ChromeOptions()
        service = Service(f"{os.path.join(os.path.dirname(__file__), 'chromedriver.exe')}")
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(10)

    def click_by_id(self, element_id: str):
        elements = self.driver.find_elements(By.ID, element_id)
        if elements:
            element = elements[0]
            if element.tag_name in ["button", "a"]:
                element.click()
                self.awaiting_redirect()
                logger.info(f"Clicked on element with id {element_id}")
            else:
                logger.warning(f"Element with id \"{element_id}\" is not clickable")
        else:
            logger.warning(f"No element found with id \"{element_id}\"")

    def click_by_class_name(self, class_name: str):
        elements = self.driver.find_elements(By.CLASS_NAME, class_name)
        if elements:
            element = elements[0]
            if element.tag_name in ["div", "li"]:
                anchor = element.find_element(By.TAG_NAME, "a")
                if anchor:
                    anchor.click()
                    self.awaiting_redirect()
                    logger.info(f"Clicked on anchor element within div with class \"{class_name}\"")
                else:
                    logger.warning(f"No anchor element found within div|li with class \"{class_name}\"")
            else:
                logger.warning(f"Element with class \"{class_name}\" is not a div|li")
        else:
            logger.warning(f"No element found with class \"{class_name}\"")

    def awaiting_redirect(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.TAG_NAME, "body"))
        )

    def go_to(self, url: str):
        self.driver.get(url)
        logger.info(f"Opened page: {url}")

    def get_current_url(self):
        return self.driver.current_url

    def close(self):
        self.driver.quit()
        logger.info("Closed the browser")
