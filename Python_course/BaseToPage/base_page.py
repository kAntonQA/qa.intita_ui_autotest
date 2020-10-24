from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    # checking the present method
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def wait_to_apeare(self, selector):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(self.selector))

    def checking_the_text_on_page(self, check):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), '" + check + "')]")))


class User:
    superadmin = "superadmin@intita.com"
    director = "director@intita.com"
    cmanager = "cmanager@qaintita.com"
    author = "author@qaintita.com"
    admin = "admin@qaintita.com"
    supervisor = "supervisor@qaintita.com"
    trainer = "trainer@qaintita.com"
    teacher = "teacher@qaintita.com"
    accountant = "accountant@qaintita.com"
    password = "qaintita"
