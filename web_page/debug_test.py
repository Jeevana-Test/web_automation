from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # go to HOME first
    page.goto("https://automationexercise.com")
    page.wait_for_timeout(3000)
    print("Step 1 - Home URL:", page.url)

    # click Signup/Login link
    page.locator("a[href='/login']").click()
    page.wait_for_timeout(2000)
    print("Step 2 - Login URL:", page.url)

    # fill credentials
    page.locator("input[data-qa='login-email']").fill("kjeevanak@gmail.com")
    page.locator("input[data-qa='login-password']").fill("Theja@123")
    print("Step 3 - filled credentials")

    # click login
    page.locator("button[data-qa='login-button']").click()
    page.wait_for_timeout(5000)
    print("Step 4 - URL after login:", page.url)
    print("Step 4 - Logged in:", page.locator("a:has-text('Logged in as')").is_visible())

    input("Press Enter to close...")
    browser.close()