import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utils.helpers import setup_logger

logger = setup_logger()

class BasePage:
    """Base class for all Page Objects. Contains shared browser actions."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url):
        logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def click(self, by, locator):
        logger.info(f"Clicking: {locator}")
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def type_text(self, by, locator, text):
        logger.info(f"Typing into {locator}: {text}")
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        element.clear()
        element.send_keys(text)

    def type_slowly(self, by, locator, text, delay=0.08):
        """Type text character by character to simulate human typing"""
        logger.info(f"Slowly typing into {locator}: {text}")
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        element.clear()
        for char in text:
            element.send_keys(char)
            time.sleep(delay)

    def get_text(self, by, locator):
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        return element.text.strip()

    def is_visible(self, by, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            return True
        except TimeoutException:
            return False

    def wait_for_url_contains(self, partial_url, timeout=15):
        logger.info(f"Waiting for URL to contain: {partial_url}")
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(partial_url)
        )

    def switch_to_new_tab(self):
        """Switch driver focus to the most recently opened tab"""
        self.driver.switch_to.window(self.driver.window_handles[-1])
        logger.info(f"Switched to new tab: {self.driver.current_url}")

    def close_current_tab_and_switch_back(self):
        """Close current tab and switch back to the previous one"""
        logger.info(f"Closing tab: {self.driver.current_url}")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        logger.info(f"Switched back to: {self.driver.current_url}")

    def scroll_to_element(self, by, locator):
        element = self.wait.until(EC.presence_of_element_located((by, locator)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_all_window_handles(self):
        return self.driver.window_handles
