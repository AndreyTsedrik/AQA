import pytest
from playwright.sync_api import sync_playwright
from tests.main_page import MainPage


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


def test_check_links(browser):
    page = browser.new_page()
    main_page = MainPage(page)

    main_page.go_to()

    # Проверка наличия ссылки "О нас"
    main_page.click_about_us()
    assert main_page.get_current_url() == "https://effective-mobile.ru/#about"  # Замените на правильный URL

    # Проверка наличия ссылки "Контакты"
    main_page.go_to()
    main_page.click_contacts()
    assert main_page.get_current_url() == "https://effective-mobile.ru/#contacts"  # Замените на правильный URL

    # Проверка наличия ссылки "Услуги"
    main_page.go_to()
    main_page.click_services()
    assert main_page.get_current_url() == "https://effective-mobile.ru/#moreinfo"  # Замените на правильный URL

    # Проверка наличия ссылки "Проекты"
    main_page.go_to()
    main_page.click_projects()
    assert main_page.get_current_url() == "https://effective-mobile.ru/#cases"  # Замените на правильный URL

    # Проверка наличия ссылки "Отзывы"
    main_page.go_to()
    main_page.click_reviews()
    assert main_page.get_current_url() == "https://effective-mobile.ru/#Reviews"  # Замените на правильный URL

    # Проверка наличия ссылки "Специалисты"
    main_page.go_to()
    main_page.click_specialist()
    assert main_page.get_current_url() == "https://effective-mobile.ru/#specialists"  # Замените на правильный URL

    page.close()
