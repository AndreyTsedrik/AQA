from playwright.sync_api import Page

class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://effective-mobile.ru/"
        self.about_us_locator = "#rec573054532 > div > div > div.t396__elem.tn-elem.tn-elem__5730545321680606406481 > a"
        self.contacts_locator = "#rec573054532 > div > div > div.t396__elem.tn-elem.tn-elem__5730545321680606406492 > a"
        self.services_locator = "#rec573054532 > div > div > div.t396__elem.tn-elem.tn-elem__5730545321680606406485 > a"
        self.projects_locator = "#rec573054532 > div > div > div.t396__elem.tn-elem.tn-elem__5730545321680606406489 > a"
        self.reviews_locator = "#rec573054532 > div > div > div.t396__elem.tn-elem.tn-elem__5730545321706704571141 > a"
        self.specialists_locator = "#rec573054532 > div > div > div.t396__elem.tn-elem.tn-elem__5730545321680606406495 > a"


    def go_to(self):
        self.page.goto(self.url)

    def click_about_us(self):
        self.page.click(self.about_us_locator)

    def click_contacts(self):
        self.page.click(self.contacts_locator)

    def click_services(self):
        self.page.click(self.services_locator)

    def click_projects(self):
        self.page.click(self.projects_locator)

    def click_reviews(self):
        self.page.click(self.reviews_locator)

    def click_specialist(self):
        self.page.click(self.specialists_locator)

    def get_current_url(self):
        return self.page.url  # Возвращает текущий URL страницы