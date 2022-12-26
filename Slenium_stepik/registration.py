from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def reg(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//div/form/div/div[1]/input")
        input1.send_keys("text1")
        input2 = browser.find_element(By.XPATH, "//div/form/div/div[2]/input")
        input2.send_keys("text2")
        input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("text3")

        # Отправляем заполненную форму
        button = browser.find_element(By.XPATH, "//div/form/button")
        button.click()

        result_reg = browser.find_element(By.XPATH, '/html/body/div/h1').text
        return result_reg

    finally:
        time.sleep(2)
        browser.quit()

if __name__ == "__main__":
    reg("https://suninjuly.github.io/registration1.html")

