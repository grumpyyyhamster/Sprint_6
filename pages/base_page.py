import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки объекта на странице')
    def waiting_for_item_to_be_visible(self, locator):
        return WebDriverWait(self.driver, 8).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Клик на объект')
    def click_on_item(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Скролл до объекта')
    def scroll_to_item(self, locator):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.driver.find_element(*locator))

    @allure.step('Ввод какого-то значения в инпут поле')
    def set_value_for_input(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('Посмотреть какой текст отображается в необходимом объекте')
    def item_text(self, locator):
        return self.driver.find_element(*locator).text
