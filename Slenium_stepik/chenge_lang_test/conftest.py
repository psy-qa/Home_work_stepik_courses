import pytest
from selenium import webdriver

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
        print("You choose fr language, start test....")
        browser = webdriver.Chrome()
        browser.get(f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    elif language == "ru":
        print("You choose ru language, start test....")
        browser = webdriver.Chrome()
        browser.get(f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    elif language == "es":
        print("You choose es language, start test....")
        browser = webdriver.Chrome()
        browser.get(f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    else:
        raise pytest.UsageError("=======you need choose lang ru of fr========")

    yield browser
    browser.quit()
    print("\n=========QUIT BROWSER=======")

