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
        self.login_button = page.locator("input[type='submit']")

    def login(self, username, password):
        self.page.goto(loginURL)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.profile_name = "#user-profile"
        self.logout_button = "#logout"

    def verify_dashboard_loaded(self):
        expect(self.page.locator(self.profile_name)).to_be_visible()

    def logout(self):
        self.page.click(self.logout_button)
        expect(self.page.locator("#login")).to_be_visible()  # Ensure redirection

