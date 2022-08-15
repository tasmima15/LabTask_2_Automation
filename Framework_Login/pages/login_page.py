import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login_lab(self, email, password):

        singin_text = self.driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        singin_text = singin_text.text
        print(singin_text)

        signIn = self.driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        signIn.click()
        time.sleep(2)

        email_field = self.driver.find_element(By.ID, 'email')
        password_field = self.driver.find_element(By.ID, 'passwd')
        login_button = self.driver.find_element(By.ID, 'SubmitLogin')

        email_field.clear()
        email_field.send_keys(email)
        time.sleep(2)

        password_field.clear()
        password_field.send_keys(password)
        time.sleep(2)

        login_button.click()
        Tshirt = self.driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]/a')
        Tshirt.click()
        time.sleep(2)

        action = ActionChains(self.driver)

        Mouse_hover = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div/div[1]/div/a[1]/img')
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

        addCart = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[1]/span')
        addCart.click()
        time.sleep(3)
        print(self.driver.title)
        time.sleep(3)
        # size = driver.find_element(By.XPATH, '//*[@id="group_1"]')
        # All_size = Select(size)
        # for all_values_size in All_size.options:
        # print(all_values_size.text)

        # All_size.select_by_value('2')
        # time.sleep(2)

        summary_checkout1 = self.driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span')
        summary_checkout1.click()
        time.sleep(2)
        print(self.driver.title)

        signIn_checkout2 = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/p[2]/a[1]/span')
        signIn_checkout2.click()
        time.sleep(2)
        print(self.driver.title)

        address_checkout3 = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/form/p/button/span')
        address_checkout3.click()
        time.sleep(2)
        print(self.driver.title)

        agree = self.driver.find_element(By.CSS_SELECTOR, '#cgv')
        agree.click()
        time.sleep(3)
        print(self.driver.title)

        payment_checkout4 = self.driver.find_element(By.XPATH, '//*[@id="form"]/p/button/span')
        payment_checkout4.click()
        time.sleep(2)
        print(self.driver.title)

        final_signOut = self.driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[2]/a')
        final_signOut.click()
        time.sleep(2)
        print(self.driver.title)

