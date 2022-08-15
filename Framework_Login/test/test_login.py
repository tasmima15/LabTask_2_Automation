import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from Framework_Login.pages.login_page import LoginPage
from Framework_Login.utils import excel_utlis


class LoginTest(unittest.TestCase):

    def test_login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("http://automationpractice.com/index.php")
        time.sleep(3)

        # Excel implementation
        file = 'D:\\SQA 7th\\automationBitm07_sir\\LabTest2_Automation\\Framework_Login\\data\\Login_data.xlsx'
        sheet = 'Sheet1'

        number_of_rows = excel_utlis.get_row_count(file, sheet)

        for r in range(2, number_of_rows + 1):
            email = excel_utlis.read_data(file, sheet, r, 1)
            password = excel_utlis.read_data(file, sheet, r, 2)

            lp = LoginPage(driver)
            lp.login_lab(email, password)

        driver.close()
