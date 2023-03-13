from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://demoqa.com')

icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')
if icon is None:
    print('Элемент не найден')
else:
    print('Элемент найден')

cards = driver.find_element(By.CSS_SELECTOR, '.category-cards > div.card')
if cards is None:
    print('Элементы не найдены')
else:
    print('Элементы найдены')

footer = driver.find_element(By.CSS_SELECTOR, '#app > footer > span')
if footer is None:
    print('Элемент не найден')
else:
    print('Элемент найден')