from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Navigate to the login page
        page.goto("https://www.saucedemo.com/")

        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Wait for results to load
        page.wait_for_selector(".inventory_list")

        # Check if results are present
        assert page.is_visible(".inventory_item")

        print("✅ Login test passed!")
        browser.close()

if __name__ == "__main__":
    test_login()
    print("All tests completed successfully.")