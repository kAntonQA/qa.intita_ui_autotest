# Class MainPageSel- store selectors from main page
class MainPageSel:
    #Selektors
    login_button = "div.header-auth > .btn"
    login_field = "email"
    password_field = "password"
    user_avatar = "#user_avatar"
    go_in = "[type='submit'].btn-auth-form"
    dropdown_menu = ".dropdown-menu-user"
    error_message = "#modalAuth > div > div > div.modal-body.p-4 > div:nth-child(1) > div:nth-child(1) > div"
    #Links
    dashbnourd = "Дошка"
    profile = "Профіль"
    exit = "Вихід"

class TupleLink:
    links = {"Курси": ".left-filter-col",
         #"Команда": ".page-title",
         #"Випускники": ".page-title",
         #"Про нас": ".about-us-header",
         #"Вакансії": ".img-responsive",
         #"Події": ".logo"
         # "Партнерам"   :,
         # "Бібліотека"  :
         }
