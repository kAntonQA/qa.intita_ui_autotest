from selenium import webdriver
import pytest
from BaseToPage.base_dashboard_page import *
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
    # mailing test
    def test_mailing(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.login_in_positive(User.cmanager, User.password)
        page.go_to_dropmenu(MainPageSel.dashbnourd)
        page = DashboardPage(browser, LINK)
        page.go_on_left_menu(LeftMenuSel.content_manager)
        page.go_to(DashPageSel.css_mailing_list_management, DashPageSel.css_mailgun)
        page = MailPage(browser, LINK)
        page.type_in_fields()


class TestForMainPage:

    # Main Page, test for main links
    def test_main_page(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.test_link_on_main_page(TupleLink.links)


class TestLoginIn:

    # Test for login pop-up, positive
    def test_user_login(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.login_in_positive(User.accountant, User.password)

    # Test for login pop-up, negative
    def test_incorrect_login(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.login_in_negative_incorrect_text("1", User.password)

    def test_incorrect_password(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.login_in_negative_incorrect_text(User.accountant, "1")

    def test_empty_login_field(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.login_in_negative_empty_field("", User.password)

    def test_empty_password_field(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.login_in_negative_empty_field(User.accountant, "")


class TestForModuleRTeacher:

    # Tests for teacher(module and course)
    def test_for_teacher_module(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.login_in_positive(User.cmanager, User.password)
        page.go_to_dropmenu(MainPageSel.dashbnourd)
        page = DashboardPage(browser, LINK)
        page.go_to(DashPageSel.css_filling_content, DashPageSel.css_course)
