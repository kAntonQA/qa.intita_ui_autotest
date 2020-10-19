from BaseToPage.base_main_page import *
from selenium.common.exceptions import NoSuchElementException
from pages.dashboard_page import *


class MainPage(BasePage):

    def test_link_on_main_page(self, tup):
        for href, check in tup.items():
            self.browser.find_element(By.LINK_TEXT, href).click()
            self.wait_to_apeare_css(check)

    def login_in_positive(self, login, password):
        self.wait_to_apeare_css(MainPageSel.login_button)
        login_link = self.browser.find_element(By.CSS_SELECTOR, MainPageSel.login_button)
        login_link.click()
        login_user = self.browser.find_element(By.NAME, MainPageSel.login_field)
        login_user.click()
        login_user.send_keys(login)
        login_pass = self.browser.find_element(By.NAME, MainPageSel.password_field)
        login_pass.click()
        login_pass.send_keys(password)
        login_to = self.browser.find_element(By.CSS_SELECTOR, MainPageSel.go_in)
        login_to.click()
        self.wait_to_apeare_css(MainPageSel.user_avatar)
        assert NoSuchElementException

    def login_in_negative_incorrect_text(self, login, password):
        self.wait_to_apeare_css(MainPageSel.login_button)
        login_link = self.browser.find_element(By.CSS_SELECTOR, MainPageSel.login_button)
        login_link.click()
        login_user = self.browser.find_element(By.NAME, MainPageSel.login_field)
        login_user.click()
        login_user.send_keys(login)
        login_pass = self.browser.find_element(By.NAME, MainPageSel.password_field)
        login_pass.click()
        login_pass.send_keys(password)
        login_to = self.browser.find_element(By.CSS_SELECTOR, MainPageSel.go_in)
        login_to.click()
        self.wait_to_apeare_css(MainPageSel.error_message)
        assert NoSuchElementException

    def login_in_negative_empty_field(self, login, password):
        self.wait_to_apeare_css(MainPageSel.login_button)
        login_link = self.browser.find_element(By.CSS_SELECTOR, MainPageSel.login_button)
        login_link.click()
        login_user = self.browser.find_element(By.NAME, MainPageSel.login_field)
        login_user.click()
        login_user.send_keys(login)
        login_pass = self.browser.find_element(By.NAME, MainPageSel.password_field)
        login_pass.click()
        login_pass.send_keys(password)
        login_to = self.browser.find_element(By.CSS_SELECTOR, MainPageSel.go_in)
        login_to.click()
        self.wait_to_apeare_css(MainPageSel.error_message)
        assert NoSuchElementException

    def go_to_dropmenu(self, link):
        self.wait_to_apeare_css(MainPageSel.user_avatar)
        dash = self.browser.find_element(By.CSS_SELECTOR, MainPageSel.dropdown_menu)
        dash.click()
        link_to = self.browser.find_element(By.LINK_TEXT, link)
        link_to.click()