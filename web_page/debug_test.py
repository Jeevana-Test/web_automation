from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://automationexercise.com/login")
    page.locator("input[data-qa='login-email']").fill("wrong@gmail.com")
    page.locator("input[data-qa='login-password']").fill("wrongpass")
    page.locator("button[data-qa='login-button']").click()
    page.wait_for_timeout(3000)
    print("URL:", page.url)
    # try different locators
    print("Locator 1:", page.locator("p[style='color: red;']").is_visible())
    print("Locator 2:", page.locator("p[style='color: red;']").count())
    print("Locator 3:", page.locator("form p").is_visible())
    print("Locator 4:", page.locator("div.login-form p").is_visible())
    input("Press Enter to close...")
    browser.close()