from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class Automation():

    def LabTask_automation(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        driver.maximize_window()
        time.sleep(2)

        singin_text = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        singin_text = singin_text.text
        print(singin_text)

        signIn = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        signIn.click()
        time.sleep(2)

        # create an account

        account_text = driver.find_element(By.XPATH, '//*[@id="create-account_form"]/h3')
        account_text = account_text.text
        print(account_text)

        # email
        email_text = driver.find_element(By.XPATH, '//*[@id="create-account_form"]/div/div[2]/label')
        email_text = email_text.text
        print(email_text)

        email = driver.find_element(By.ID, 'email_create')
        email.clear()
        email.send_keys("shafu34223@gmail.com")
        time.sleep(2)

        # create button

        createBtn = driver.find_element(By.ID, 'SubmitCreate')
        createBtn.click()
        time.sleep(5)

        # title

        driver.find_element(By.ID, 'id_gender1').click()
        time.sleep(5)
        Mrs = driver.find_element(By.ID, 'id_gender1').is_selected()
        print(Mrs)
        time.sleep(3)

        # firstname

        Firstname = driver.find_element(By.ID, 'customer_firstname')
        Firstname.send_keys('Shafu')
        time.sleep(2)

        Lastname = driver.find_element(By.ID, 'customer_lastname')
        Lastname.send_keys('Rahman')
        time.sleep(2)

        # email1 = driver.find_element(By.XPATH, '//*[@id="email"]')
        # email1.clear()
        # email1.send_keys('tasmima12@gmail.com')
        # time.sleep(2)

        password = driver.find_element(By.ID, 'passwd')
        password.send_keys('22222')
        time.sleep(2)

        # date

        Date = driver.find_element(By.XPATH, '//*[@id="days"]')
        All_date = Select(Date)
        for all_values in All_date.options:
            print(all_values.text)

        All_date.select_by_value('7')
        time.sleep(2)

        Months = driver.find_element(By.XPATH, '//*[@id="months"]')
        All_months = Select(Months)
        for all_values_months in All_months.options:
            print(all_values_months.text)

        All_months.select_by_value('2')
        time.sleep(2)

        years = driver.find_element(By.XPATH, '//*[@id="years"]')
        All_years = Select(years)
        for all_values_year in All_years.options:
            print(all_values_year.text)

        All_years.select_by_value('1992')
        time.sleep(2)

        company = driver.find_element(By.ID, 'company')
        company.send_keys('Alaksa LTM')
        time.sleep(2)

        address = driver.find_element(By.ID, 'address1')
        address.send_keys('Main Street,Anchorage,Alaksa ltd ')
        time.sleep(2)

        city = driver.find_element(By.ID, 'city')
        city.send_keys('Anchorage')
        time.sleep(2)

        states = driver.find_element(By.XPATH, '//*[@id="id_state"]')
        All_states = Select(states)
        for all_values_states in All_states.options:
            print(all_values_states.text)

        All_states.select_by_value('5')
        time.sleep(2)

        postal_code = driver.find_element(By.ID, 'postcode')
        postal_code.send_keys('99501')
        time.sleep(2)

        country = driver.find_element(By.XPATH, '//*[@id="id_country"]')
        All_country = Select(country)
        for all_values_country in All_country.options:
            print(all_values_country.text)

        All_country.select_by_value('21')
        time.sleep(2)

        addition_phn = driver.find_element(By.XPATH, '//*[@id="other"]')
        addition_phn.send_keys("0193294892")
        time.sleep(2)

        mobile = driver.find_element(By.XPATH, '//*[@id="phone_mobile"]')
        mobile.send_keys('019128767')
        time.sleep(2)

        refernce = driver.find_element(By.XPATH, '//*[@id="alias"]')
        refernce.clear()
        refernce.send_keys("My company")
        time.sleep(2)

        # Profile

        register = driver.find_element(By.XPATH, '//*[@id="submitAccount"]')
        register.click()
        time.sleep(2)

        signOut = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[2]/a')
        signOut.click()
        time.sleep(2)

        singin_text = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        singin_text = singin_text.text
        print(singin_text)

        signIn = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        signIn.click()
        time.sleep(2)

        email = driver.find_element(By.ID, 'email')
        email.clear()
        email.send_keys("shafat12@gmail.com")
        time.sleep(2)

        password = driver.find_element(By.ID, 'passwd')
        password.send_keys('22222')
        time.sleep(2)

        signIn = driver.find_element(By.ID, 'SubmitLogin')
        signIn.click()
        time.sleep(3)

        Tshirt = driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]/a')
        Tshirt.click()
        time.sleep(2)

        action = ActionChains(driver)

        Mouse_hover = driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div/div[1]/div/a[1]/img')
        action.move_to_element(Mouse_hover).perform()
        time.sleep(2)

        # quick_view = driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div/div[1]/div/a[2]')
        # quick_view.click()
        # time.sleep(2)
        # print(driver.title)

        # driver.find_element(By.ID, 'color_2').click()
        # time.sleep(3)
        # blue = driver.find_element(By.ID, 'color_2').is_selected()
        # print(blue)
        # time.sleep(3)

        # blue_actions = ActionChains(driver)

        # blue_hover = driver.find_element(By.ID, 'thumb_3')
        # blue_actions.move_to_element(blue_hover).perform()
        # time.sleep(2)
        # blue_hover.click()
        # time.sleep(2)

        # cart_actions = ActionChains(driver)

        # cart_hover = driver.find_element(By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a')
        # cart_actions.move_to_element(cart_hover).perform()
        # time.sleep(2)

        # check = driver.find_element(By.ID, 'button_order_cart')
        # check.click()
        # time.sleep(2)

        # quantity = driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]')
        # quantity.click()
        # time.sleep(2)

        # quantity.clear()
        # time.sleep(1)
        # quantity.send_keys('2')
        # time.sleep(2)

        addCart = driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[1]/span')
        addCart.click()
        time.sleep(3)
        print(driver.title)
        time.sleep(2)
        # size = driver.find_element(By.XPATH, '//*[@id="group_1"]')
        # All_size = Select(size)
        # for all_values_size in All_size.options:
        # print(all_values_size.text)

        # All_size.select_by_value('2')
        # time.sleep(2)

        summary_checkout1 = driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span')
        summary_checkout1.click()
        time.sleep(2)
        print(driver.title)

        signIn_checkout2 = driver.find_element(By.XPATH, '//*[@id="center_column"]/p[2]/a[1]/span')
        signIn_checkout2.click()
        time.sleep(2)
        print(driver.title)

        address_checkout3 = driver.find_element(By.XPATH, '//*[@id="center_column"]/form/p/button/span')
        address_checkout3.click()
        time.sleep(2)
        print(driver.title)

        agree = driver.find_element(By.CSS_SELECTOR, '#cgv')
        agree.click()
        time.sleep(2)
        print(driver.title)

        payment_checkout4 = driver.find_element(By.XPATH, '//*[@id="form"]/p/button/span')
        payment_checkout4.click()
        time.sleep(2)
        print(driver.title)

        final_signOut = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[2]/a')
        final_signOut.click()
        time.sleep(2)
        print(driver.title)

        driver.close()


obj = Automation()
obj.LabTask_automation()
