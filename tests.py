from conftest import BANK_SITE_URL
from pages.google_page import GoogleSearchHelper
from pages.mtc_bank_page import MTCBankPage


def test_mtc_bank(browser):
    google_search_page = GoogleSearchHelper(browser, "https://www.google.com/")
    google_search_page.go_to_site()
    google_search_page.search("МТС Банк")
    element = google_search_page.get_result_item_by_url(BANK_SITE_URL)
    assert element is not None and element.get_attribute("href") == BANK_SITE_URL

    mtc_bank_page = MTCBankPage(browser, element.get_attribute("href"))
    mtc_bank_page.go_to_site()
    deposits_tab = mtc_bank_page.get_deposits_tab()
    assert deposits_tab is not None
    mtc_bank_deposits_page = MTCBankPage(browser, deposits_tab.get_attribute("href"))
    mtc_bank_deposits_page.go_to_site()
    deposit_urls = mtc_bank_page.get_deposit_urls()

    assert isinstance(deposit_urls, list) and len(deposit_urls) > 0
    specific_deposits_page = MTCBankPage(browser, deposit_urls[1])
    specific_deposits_page.go_to_site()
    specific_deposits_page.fill_form()
    specific_deposits_page.go_to_url(BANK_SITE_URL)
