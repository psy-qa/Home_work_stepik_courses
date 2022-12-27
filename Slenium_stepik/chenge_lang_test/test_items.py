from selenium.webdriver.common.by import By

def test_button_value_in_page(browser):
    """Check button ang attributes button in page"""
    button = browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
    button_text = button.get_attribute("value")

    assert button_text == "Ajouter au panier" or button_text == "Добавить в корзину", "ERROR ASSER TEXT BUTTON"
