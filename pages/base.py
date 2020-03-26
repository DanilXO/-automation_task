from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
        Parent class for all pages.
        Uses: browser driver and page url
    """
    def __init__(self, driver, page_url):
        self.driver = driver
        self.page_url = page_url

    def find_element(self, locator, time=10):
        """
        Find element by locator
        :param locator: selenium locator
        :param time: max searching time
        :return: selenium element
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        """
        Find elements by locator
        :param locator: selenium locator
        :param time: max searching time
        :return: selenium elements
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.page_url)

    def go_to_url(self, url_path):
        return self.driver.get(url_path)
