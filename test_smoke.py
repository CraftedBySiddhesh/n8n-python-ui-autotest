from playwright.sync_api import sync_playwright

def test_saucedemo_login_smoke():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/", timeout=30000)

        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        page.wait_for_selector(".inventory_list", timeout=10000)

        browser.close()
