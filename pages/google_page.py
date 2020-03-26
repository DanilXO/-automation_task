from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base import BasePage


class GoogleSearchLocators:
    """
    class for defining locators
    """
    LOCATOR_GOOGLE_SEARCH_FIELD = (By.CLASS_NAME, "gLFyf")

    @staticmethod
    def get_href_locator(href_value):
        return By.XPATH, f"//a[contains(@href,\'{href_value}\')]"


class GoogleSearchHelper(BasePage):
    """
    Google helper class
    """
    def search(self, search_text):
        """
        Submits a search request through the form
        :param search_text: what need to find
        :return: selenium element
        """
        search_field = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(search_text)
        search_field.send_keys(Keys.ENTER)
        return search_field

    def get_result_item_by_url(self, url):
        """
        Finds an element with href equal to url
        :param url: what url need to find
        :return: selenium element
        """
        try:
            return self.find_element(GoogleSearchLocators.get_href_locator(url))
        except TimeoutException:
            return None
