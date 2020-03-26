from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base import BasePage


class MTCBankLocators:
    """
    class for defining locators
    """
    LOCATOR_DEPOSIT_LINKS = (By.XPATH, '//div[contains(@class, "depo-note-links")]//a[contains(@href, "__form")]')

    LOCATOR_FORM_FIO_FIELD = (By.ID, 'dadataFIO')
    LOCATOR_FORM_PHONE_FIELD = (By.ID, 'mts2-section-form__mobilephone')
    LOCATOR_FORM_CITY_FIELD = (By.ID, 'cities')
    LOCATOR_FORM_DEPARTMENT_FIELD = (By.ID, 'affiliates')
    LOCATOR_FORM_EMAIL_FIELD = (By.ID, 'mts2-section-form__email')
    LOCATOR_FORM_PROMO_FIELD = (By.ID, 'mts2-section-form__promo')

    @staticmethod
    def get_tab_locators_by_name(tab_name):
        """
        returns locator by text in link
        :param tab_name: a-params text
        :return: selenium locator
        """
        return By.LINK_TEXT, tab_name


class MTCBankPage(BasePage):
    """
    Bank page class helper
    """
    deposit_urls_with_anchor = []

    def get_nav_tab_by_name(self, name):
        """
        returns a menu item with the specified name
        :param name: tab name
        :return: selenium element
        """
        try:
            return self.find_element(MTCBankLocators.get_tab_locators_by_name(name))
        except TimeoutException:
            return None

    def get_deposits_tab(self):
        """
        returns a menu item with the "Вклады" name
        :return: selenium element
        """
        return self.get_nav_tab_by_name("Вклады")

    def get_deposit_urls(self):
        """
        Fills out and returns links with deposits with an anchor link to the form
        :return: list of urls
        """
        try:
            elements = self.find_elements(MTCBankLocators.LOCATOR_DEPOSIT_LINKS, time=20)
            for element in elements:
                self.deposit_urls_with_anchor.append(element.get_attribute("href"))
            return self.deposit_urls_with_anchor
        except TimeoutException:
            return self.deposit_urls_with_anchor

    def fill_form(self, fio="Фролов Даниил Дмитриевич", phone="8800853535", city="Тольятти",
                  email='byka72@gmail.com', department='Отделение', promo=12341234):
        """
        Fills the form with the specified values
        """
        fio_field = self.find_element(MTCBankLocators.LOCATOR_FORM_FIO_FIELD)
        fio_field.click()
        fio_field.send_keys(fio)

        phone_field = self.find_element(MTCBankLocators.LOCATOR_FORM_PHONE_FIELD)
        phone_field.click()
        phone_field.send_keys(phone)

        city_field = self.find_element(MTCBankLocators.LOCATOR_FORM_CITY_FIELD)
        city_field.click()
        city_field.send_keys(city)

        try:
            depart_field = Select(self.find_element(MTCBankLocators.LOCATOR_FORM_DEPARTMENT_FIELD))
            depart_field.select_by_value(department)
            # TODO: Обратите внимание на вашу форму! Select без значений - http://joxi.ru/vAWQ4j4SqozMqm
        except NoSuchElementException:
            pass

        email_field = self.find_element(MTCBankLocators.LOCATOR_FORM_EMAIL_FIELD)
        email_field.click()
        email_field.send_keys(email)

        promo_field = self.find_element(MTCBankLocators.LOCATOR_FORM_PROMO_FIELD)
        promo_field.click()
        promo_field.send_keys(promo)


