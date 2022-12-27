import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="choose language : fr or ru")


@pytest.fixture(autouse=True)
def invite_print():
    print("\nwelcome to KAZANTIP.....\n")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language == "fr":
        print('\n You choose fr language, start test....')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    elif language == "ru":
        print("You choose ru language, start test....")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    elif language == "es":
        print("You choose es language, start test....")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    else:
        raise pytest.UsageError("=======you need choose lang ru, es or fr========")

    yield browser
    browser.quit()
    print("\n=========QUIT BROWSER=======")

