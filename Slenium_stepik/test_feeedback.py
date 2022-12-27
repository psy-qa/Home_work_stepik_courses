import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

links = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1"])
@pytest.mark.xfail
def test_feedback(browser, link):
    """test feed back """
    try:
        answer = math.log(int(time.time()))
        browser.get(link)
        browser.implicitly_wait(15)

        enter_button = browser.find_element(By.XPATH, '//*[@id="ember33"]')
        print("button before click")
        enter_button.click()
        print("after button click")

        email_input = browser.find_element(By.XPATH, '//*[@id="id_login_email"]')
        email_input.send_keys("ravehazard1@gmail.com")
        print("email input")

        password_input = browser.find_element(By.XPATH, '//*[@id="id_login_password"]')
        password_input.send_keys("356622722")
        print("password input")
        time.sleep(2)

        enter_auth = browser.find_element(By.XPATH, '//*[@id="login_form"]/button')
        print("find button enter")
        enter_auth.click()
        print("button clicked")
        time.sleep(3)

        #enter_answer = browser.find_element(By.XPATH, '//*[@id="ember103"]')
        enter_answer = browser.find_element(By.XPATH, '/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[2]/div/div/div/textarea')
        print('2222')
        print('3333')
        enter_answer.click()
        print('4444')
        enter_answer.send_keys(str(answer))
        print('555')


        send_answer = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                  '//*[@id="ember79"]/div/section/div/div[1]/div[3]/button')))
        send_answer.click()

        result1 = browser.find_element(By.XPATH, '//*[@id="ember104"]/p').text
        print(result1)

        assert result1 == "Correct!", "wrong answer"

    finally:
        relog = browser.find_element(By.XPATH, '//*[@id="ember39"]/button/img')
        relog.click()
        time.sleep(2)
