import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from Framework_Register.pages_register.register_page import RegisterPage
from Framework_Register.Register_utils import register_utils


class RegisterTest(unittest.TestCase):

    def test_register(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("http://automationpractice.com/index.php")
        time.sleep(3)

        # Excel implementation
        file = 'D:\\SQA 7th\\automationBitm07_sir\\LabTest2_Automation\\Framework_Register\\data_register\\Register_data.xlsx'
        sheet = 'Sheet1'

        number_of_rows = register_utils.get_row_count(file, sheet)

        for r in range(2, number_of_rows + 1):
            emails = register_utils.read_data(file, sheet, r, 1)
            firstname = register_utils.read_data(file, sheet, r, 2)
            lastname = register_utils.read_data(file, sheet, r, 3)
            passwords = register_utils.read_data(file, sheet, r, 4)
            company = register_utils.read_data(file, sheet, r, 5)
            address = register_utils.read_data(file, sheet, r, 6)
            city = register_utils.read_data(file, sheet, r, 7)
            postal_code = register_utils.read_data(file, sheet, r, 8)
            addition = register_utils.read_data(file, sheet, r, 9)
            mobile = register_utils.read_data(file, sheet, r, 10)
            reference = register_utils.read_data(file, sheet, r, 11)

            rp = RegisterPage(driver)
            rp.register_lab(emails, firstname, lastname, passwords, company,
                            address, city, postal_code, addition, mobile, reference)

        driver.close()
