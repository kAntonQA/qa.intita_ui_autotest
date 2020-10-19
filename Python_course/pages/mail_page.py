from selenium.webdriver.support.ui import Select
from BaseToPage.base_mail_page import *
from BaseToPage.base_page import *
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
            selec = self.browser.find_elements(By.CSS_SELECTOR, Field.get_the_number_of_chouse)

            for elem in selec:
                self.browser.find_element(By.CSS_SELECTOR, Field.for_hoo).click()
                self.wait_to_apeare_css(Field.get_the_number_of_chouse)
                elem.click()
