import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("Проверка заголовка")
def test_start_page():
    driver = webdriver.Chrome()
    driver.get("https://rpaqp-ultimate-tester.github.io/Kish_Loren.html")
    assert driver.title == "Рецепт Киш Лорен"

    with allure.step("Закрытие браузера"):
        driver.quit()

@allure.title("Проверка названия блюда")
def test_name_recipe():
    assert driver.find_element(By.TAG_NAME, "h1").text == "Пирог с лососем и сыром (киш лорен)"

    with allure.step("Проверка ингридиентов"):

    assert driver.find_element(By.TAG_NAME, "h2").text == "Ингридиенты на форму диаметром 26-28см:"

    with allure.step("Ингридиенты для теста"):

    assert driver.find_element(By.TAG_NAME, "h3").text == "Для теста:"
