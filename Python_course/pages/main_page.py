from BaseToPage.base_main_page import *
import time
from pages.dashboard_page import *


class MainPage(BasePage):
    def test_link_on_main_page(self, tup):
        for href, check in tup.items():
            self.browser.find_element(By.LINK_TEXT, href).click()
            self.wait_to_apeare_css(check)

    def login_in(self, login, password, check, err):
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

        if check != 0:
            self.wait_to_apeare_css(check)

        if err != 0:
            self.wait_to_apeare_xpath(err)

    def go_to_dropmenu(self, link):
        self.wait_to_apeare_css(MainPageSel.user_avatar)
        dash = self.browser.find_element(By.CSS_SELECTOR, MainPageSel.dropdown_menu)
        dash.click()
        link_to = self.browser.find_element(By.LINK_TEXT, link)
        link_to.click()