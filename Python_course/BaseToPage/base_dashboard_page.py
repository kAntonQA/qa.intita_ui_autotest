class DashPageSel:
    # Керування розсилками
    css_filling_content = " div:nth-child(1) > div > div > div > div > div:nth-child(1) > span.basic-header"
    css_course = "#hidden-content > div > div:nth-child(1) > a"
    # Наповнення контенту
    css_mailing_list_management = "div:nth-child(2) > div > div > div > div > div:nth-child(1) > span.basic-header"
    css_mailgun = "#hidden-content > div > div:nth-child(1) > a"

class LeftMenuSel:
    director = ".nav-link[href = '#/director']"
    super_admin = ".nav-link[href = '#/super_admin']"
    admin = ".nav-link[href = '#/admin']"
    content_manager = ".nav-link[href = '#/content_manager']"
    supervisor = ".nav-link[href = '#/supervisor']"
    notification = ".nav-link[href = '#/notification']"
    profile = ".nav-link[href = '#/profile']"