from selenium import webdriver
import pytest
from BaseToPage.base_dashboard_page import *
from pages.dashboard_page import *
from pages.mail_page import *
from pages.main_page import *


LINK = "https://qa.intita.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMailgun:

    def test_mailing(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.login_in(User.cmanager, User.password, 0, 0)
        page.go_to_dropmenu(MainPageSel.dashbnourd)
        page = DashboardPage(browser, LINK)
        page.go_on_left_menu(LeftMenuSel.content_manager)
        page.go_to(DashPageSel.css_mailing_list_management, DashPageSel.css_mailgun)
        page = MailPage(browser, LINK)
        page.type_in_field()
        time.sleep(3)


def est_main_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.test_link_on_main_page(TupleLink.links)
    time.sleep(3)


class estForMainPage:
    # Main Page tests (before login-in)

    # Test for login pop-up
    def test_user_login(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.login_in(User.accountant, User.password, MainPageSel.user_avatar, 0)

    def test_incorrect_login(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.login_in("1", User.password, 0, "Невірна")

    def test_incorrect_password(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.login_in(User.accountant, "1", 0, "Невірна")

    def test_empty_login_field(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.login_in("", User.password, 0, "заповни")

    def test_empty_password_field(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.login_in(User.accountant, "", 0, "заповни")


class estForModuleRTeacher:
    # Tests for teacher(module and course)
    def test_for_teacher_module(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.login_in(User.cmanager, User.password, MainPageSel.user_avatar, 0)
        page.go_to_dropmenu(MainPageSel.dashbnourd)
        page = DashboardPage(browser, LINK)
        page.go_to(DashPageSel.css_filling_content, DashPageSel.css_course)
        time.sleep(3)
