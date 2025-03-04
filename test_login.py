import pytest
from playwright.sync_api import Page, sync_playwright, expect
from dotenv import load_dotenv
import os

load_dotenv()

uname = os.getenv("NAMA")
passwd = os.getenv("PASSWD")

# def test_login(page:Page):
#     #launch browser
#     page.goto("http://solehudindt.pythonanywhere.com/dev/login/")
#     page.get_by_role("textbox", name="Username:").click()
#     page.get_by_role("textbox", name="Username:").fill("solehudindt")
#     page.get_by_role("textbox", name="Password:").click()
#     page.get_by_role("textbox", name="Password:").fill("./bl0g2109")
#     page.get_by_role("button", name="Log in").click()
#     assert page.get_by_text("solehudindt").is_visible()
from models.login_scenario import LoginPage, DashboardPage

def test_valid_login(page):
    # browser = p.chromium.launch(headless=False)  # Change to True for headless mode
    # page = browser.new_page()

    login_page = LoginPage(page)
    login_page.login(uname, passwd)  # Use valid test credentials

    dashboard = DashboardPage(page)
    dashboard.verify_dashboard_loaded()
    dashboard.logout()
    # assert page.get_by_text("WELCOME").is_visible()
    # assert page.url == "https://solehudindt.pythonanywhere.com/"

def test_invalid_login(page):

    # page = browser.new_page()
    
    login_page = LoginPage(page)
    login_page.login("testuser", "wrongpassword")
    
    expect(page.locator(".errornote")).to_contain_text("correct username")
    page.screenshot(path="galat.png")