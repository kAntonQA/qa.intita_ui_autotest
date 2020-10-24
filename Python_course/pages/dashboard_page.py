from BaseToPage.base_page import *


class DashboardPage(BasePage):
    def go_to(self, menu, submenu):
        self.wait_to_apeare(menu)
        go_to_menu = self.browser.find_element(By.CSS_SELECTOR, menu)
        go_to_menu.click()
        self.wait_to_apeare(submenu)
        go_to_submenu = self.browser.find_element(By.CSS_SELECTOR, submenu)
        go_to_submenu.click()

    def go_on_left_menu(self, sel):
        self.wait_to_apeare(sel)
        go_to_menu = self.browser.find_element(By.CSS_SELECTOR, sel)
        go_to_menu.click()
