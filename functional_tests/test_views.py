import os
from pathlib import Path

import environ
import pytest
from playwright.sync_api import sync_playwright

env = environ.Env(
    LOGIN_USERNAME=str,
    LOGIN_PASSWORD=str,
)
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


def test_E2E_login():
    with sync_playwright() as play:
        browser = play.chromium.launch()
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000/")
        page.click("text=Log In")
        assert page.inner_text("h2") == "Login"
        page.fill("input[name=username]", env("LOGIN_USERNAME"))
        page.fill("input[name=password]", env("LOGIN_PASSWORD"))
        page.click("input[value=Login]")

        assert "List Item" in page.inner_text()
        page.screenshot(path="screenshots/screenshot.png")
        browser.close("ul")


@pytest.mark.skip(reason="working on a complete test")
def test_E2E_login_credentials():
    with sync_playwright() as play:
        browser = play.chromium.launch()
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000/")
        page.fill("input[name=username]", env("LOGIN_USERNAME"))
        page.fill("input[name=password]", env("LOGIN_PASSWORD"))
        page.click("input[value=Login]")
        assert "List Item" in page.inner_text()
        assert page.inner_text("a[class=main__link]") == "test 1"
        # need a more specific selector here


@pytest.mark.skip(reason="currently broken in docker due to deps")
def test_E2E_create_listing(listing_fixture):
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000/create/")
        page.fill("input[name=title]", listing_fixture.title)
        page.fill("input[name=description]", listing_fixture.description)
        page.fill("input[name=start_price]", listing_fixture.start_price)
        page.fill("input[name=image]", listing_fixture.image)
        page.locator("button", has_text="submit").click()
        assert page.url == "http://127.0.0.1:8000/"
        # assert page.locator()
        browser.close()
