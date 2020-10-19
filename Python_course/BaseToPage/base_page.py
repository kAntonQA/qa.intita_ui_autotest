from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def wait_to_apeare_css(self, selector):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_to_apeare_xpath(self, check):
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
