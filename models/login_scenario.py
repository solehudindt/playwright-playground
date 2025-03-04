from playwright.sync_api import Page, expect
from dotenv import load_dotenv
import os

load_dotenv()

loginURL = os.getenv("LOGIN_URL")

# pake pytest(Page)
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_label("Username:")
        self.password_input = page.get_by_label("Password:")
        # self.username_input = page.locator("#id_username")
        # self.password_input = page.locator("#id_password")
        self.login_button = page.locator("input[type='submit']")

    def login(self, username, password):
        self.page.goto(loginURL)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.greeting = page.locator("#user-tools")
        self.logout_button = page.get_by_role("link", name="Log Out")

    def verify_dashboard_loaded(self):
        expect(self.greeting).to_contain_text("Welcome")

    def logout(self):
        self.logout_button.click()
        expect(self.page.get_by_text("Logged out")).to_be_visible()

