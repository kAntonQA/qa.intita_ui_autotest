from selenium.webdriver.common.by import By

class MainPageLocators():

    # Selectors on main page
    login_button = (By.CSS_SELECTOR, "div.header-auth > .btn")
    user_avatar = (By.CSS_SELECTOR, "#user_avatar")
    go_in = (By.CSS_SELECTOR, "[type='submit'].btn-auth-form")
    dropdown_menu = (By.CSS_SELECTOR, ".dropdown-menu-user")

    # selectors on sign-in pop-up
    login_field = (By.NAME, "email")
    password_field = (By.NAME, "password")
    error_message = (By.CSS_SELECTOR, ".text-danger.input-error.error-position")

    # Links on dashboard
    dashbnourd = (By.LINK_TEXT, "Дошка")
    profile = (By.LINK_TEXT, "Профіль")
    exit = (By.LINK_TEXT, "Вихід")

    # link on top of the page
    links = {"Курси": ".left-filter-col",
             "Команда": ".page-title",
             "Випускники": ".page-title",
             "Про нас": ".about-us-header",
             "Вакансії": ".img-responsive",
             "Події": ".logo"
             # "Партнерам"   :,
             # "Бібліотека"  :
             }