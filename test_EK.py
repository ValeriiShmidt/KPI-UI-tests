from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Tests(TestCase):
    def test_EK(self):
        search_request = 'macbook'
        url = 'https://ek.ua/ua/'

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.implicitly_wait(10)

        browser.get(url)

        browser.find_element_by_css_selector('[id="ek-search"]').send_keys(search_request)
        browser.find_element_by_css_selector('[id="ek-search"]').send_keys(Keys.ENTER)

        actualResult = browser.find_element_by_css_selector('[id="search_title"]').text

        expectedResult = search_request

        assert expectedResult in actualResult

        browser.close()