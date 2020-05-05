from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = browser.find_element_by_id("submit_button")

def test_1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/simple_form_find_task.html")
        button = browser.find_element(By.ID, "submit_button")
        button.click()
        # time.sleep(2)
    finally:
        browser.quit()


def test_2():
    link = 'http://suninjuly.github.io/simple_form_find_task.html'
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        input_1 = browser.find_element_by_tag_name("input")
        input_1.send_keys("Ivan")
        input2 = browser.find_element_by_name("last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name("city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_id("country")
        input4.send_keys("Russia")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
    finally:
        time.sleep(15)
        browser.quit()


def test_3():
    link = 'https://www.degreesymbol.net/'

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        find_link = browser.find_element_by_link_text('» Degree symbol examples')
        find_link.click()
    finally:
        time.sleep(5)
        browser.quit()


def test_4():
    link = 'http://suninjuly.github.io/find_link_text'
    url = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        find_str = browser.find_element_by_link_text(str(url))
        find_str.click()

        input_1 = browser.find_element_by_tag_name("input")
        input_1.send_keys("Ivan")
        input2 = browser.find_element_by_name("last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name("city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_id("country")
        input4.send_keys("Russia")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    finally:
        time.sleep(15)
        browser.quit()


def test_5():
    link = 'http://suninjuly.github.io/huge_form.html'
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        elements = browser.find_elements_by_tag_name("input")
        for element in elements:
            element.send_keys("boobooboo")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


def test_6():
    link = 'http://suninjuly.github.io/find_xpath_form'
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        input_1 = browser.find_element_by_tag_name("input")
        input_1.send_keys("Ivan")
        input2 = browser.find_element_by_name("last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name("city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_id("country")
        input4.send_keys("Russia")
        button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
        button.click()
    finally:
        time.sleep(15)
        browser.quit()
