from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys
from BaseToPage.base_mail_page import *
from BaseToPage.base_page import *
# import time
# from selenium.common.exceptions import NoSuchElementException


class MailPage(BasePage):

    def type_in_fields(self):

        element = self.browser.find_element(By.ID, "mailType")
        drp = Select(element)
        all_options = drp.options

        for option in all_options:
            drp.select_by_visible_text(option.text)

            if option.text == "Розсилка по базі email`ів":
                break

            print(f"\n-=Start testing: {option.text}=-")
            get_the_users = self.browser.find_elements(By.CSS_SELECTOR, MailPafeField.get_the_number_of_chouse)

            for user in get_the_users:

                if len(get_the_users) == 0:
                    self.browser.find_element(By.CSS_SELECTOR, MailPafeField.for_whom_the_newsletter).click()
                    self.wait_to_apeare(MailPafeField.for_whom_the_newsletter)
                    self.browser.find_element(By.CSS_SELECTOR, "#recipients").send_keys("a")
                    self.wait_to_apeare(MailPafeField.for_whom_the_newsletter)
                    self.browser.find_element(By.CSS_SELECTOR, "#recipients").clear()

                self.browser.find_element(By.CSS_SELECTOR, MailPafeField.for_whom_the_newsletter).click()
                self.wait_to_apeare(MailPafeField.get_the_number_of_chouse)
                user.click()

            them = self.browser.find_element(By.ID, MailPafeField.them_field_id)
            them.clear()
            them.send_keys(option.text)
            self.browser.find_element(By.CSS_SELECTOR, MailPafeField.text_field_css).send_keys(option.text)
