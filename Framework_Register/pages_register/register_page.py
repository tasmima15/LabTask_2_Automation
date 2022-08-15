import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class RegisterPage():

    def __init__(self, driver):
        self.driver = driver

    def register_lab(self, emails, firstname, lastname, passwords, company,
                     address, city, postal_code, addition, mobile, reference):

        singin_text = self.driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        singin_text = singin_text.text
        print(singin_text)

        signIn = self.driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        signIn.click()
        time.sleep(2)

        # create an account

        account_text = self.driver.find_element(By.XPATH, '//*[@id="create-account_form"]/h3')
        account_text = account_text.text
        print(account_text)

        # email
        email_text = self.driver.find_element(By.XPATH, '//*[@id="create-account_form"]/div/div[2]/label')
        email_text = email_text.text
        print(email_text)

        email_field = self.driver.find_element(By.ID, 'email_create')
        email_field.clear()
        email_field.send_keys(emails)
        time.sleep(2)

        # create button

        createBtn = self.driver.find_element(By.ID, 'SubmitCreate')
        createBtn.click()
        time.sleep(5)

        # title

        self.driver.find_element(By.ID, 'id_gender1').click()
        time.sleep(5)
        Mrs = self.driver.find_element(By.ID, 'id_gender1').is_selected()
        print(Mrs)
        time.sleep(3)

        # firstname

        Firstname_field = self.driver.find_element(By.ID, 'customer_firstname')
        Firstname_field.send_keys(firstname)
        time.sleep(2)

        Lastname_field = self.driver.find_element(By.ID, 'customer_lastname')
        Lastname_field.send_keys(lastname)
        time.sleep(2)

        # email1 = driver.find_element(By.XPATH, '//*[@id="email"]')
        # email1.clear()
        # email1.send_keys('tasmima12@gmail.com')
        # time.sleep(2)

        password_field = self.driver.find_element(By.ID, 'passwd')
        password_field.send_keys(passwords)
        time.sleep(2)

        # date

        Date_field = self.driver.find_element(By.XPATH, '//*[@id="days"]')
        All_date = Select(Date_field)
        for all_values in All_date.options:
            print(all_values.text)

        All_date.select_by_value('4')
        time.sleep(2)

        Months_field = self.driver.find_element(By.XPATH, '//*[@id="months"]')
        All_months = Select(Months_field)
        for all_values_months in All_months.options:
            print(all_values_months.text)

        All_months.select_by_value('12')
        time.sleep(2)

        years_field = self.driver.find_element(By.XPATH, '//*[@id="years"]')
        All_years = Select(years_field)
        for all_values_year in All_years.options:
            print(all_values_year.text)

        All_years.select_by_value('2000')
        time.sleep(2)

        company_field = self.driver.find_element(By.ID, 'company')
        company_field.send_keys(company)
        time.sleep(2)

        address_field = self.driver.find_element(By.ID, 'address1')
        address_field.send_keys(address)
        time.sleep(2)

        city_field = self.driver.find_element(By.ID, 'city')
        city_field.send_keys(city)
        time.sleep(2)

        states_field = self.driver.find_element(By.XPATH, '//*[@id="id_state"]')
        All_states = Select(states_field)
        for all_values_states in All_states.options:
            print(all_values_states.text)

        All_states.select_by_value('3')
        time.sleep(2)

        postal_code_field = self.driver.find_element(By.ID, 'postcode')
        postal_code_field.send_keys(postal_code)
        time.sleep(2)

        country_field = self.driver.find_element(By.XPATH, '//*[@id="id_country"]')
        All_country = Select(country_field)
        for all_values_country in All_country.options:
            print(all_values_country.text)

        All_country.select_by_value('21')
        time.sleep(2)

        addition_phn = self.driver.find_element(By.XPATH, '//*[@id="other"]')
        addition_phn.send_keys(addition)
        time.sleep(2)

        mobile_field = self.driver.find_element(By.XPATH, '//*[@id="phone_mobile"]')
        mobile_field.send_keys(mobile)
        time.sleep(2)

        refernce_field = self.driver.find_element(By.XPATH, '//*[@id="alias"]')
        refernce_field.clear()
        refernce_field.send_keys(reference)
        time.sleep(2)

        # Profile

        register = self.driver.find_element(By.XPATH, '//*[@id="submitAccount"]')
        register.click()
        time.sleep(2)

        signOut = self.driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[2]/a')
        signOut.click()
        time.sleep(2)
