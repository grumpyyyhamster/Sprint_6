import allure

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step('Клик на "Заказать" в хедере')
    def click_on_header_order_button(self):
        self.click_on_item(HomePageLocators.HEADER_ORDER_BUTTON)

    @allure.step('Клик на "Заказать" на главной странице')
    def click_on_home_order_button(self):
        self.click_on_item(HomePageLocators.ORDER_BUTTON)

    @allure.step('Скролл до секции "Вопросы о важном"')
    def scroll_to_faq(self):
        self.scroll_to_item(HomePageLocators.FAQ_SECTION)

    @allure.step('Клик на необходимый вопрос ("Вопросы о важном")')
    def click_on_question_in_faq(self, value):
        self.click_on_item(HomePageLocators.QUESTIONS[value])

    @allure.step('Ожидание загрузки ответа ("Вопросы о важном")')
    def waiting_for_item_to_be_visible_faq(self, value):
        self.waiting_for_item_to_be_visible(HomePageLocators.ANSWERS[value])

    @allure.step('Посмотреть какой текст отображается в необходимом объекте ("Вопросы о важном")')
    def item_text_faq(self, value):
        return self.item_text(HomePageLocators.ANSWERS[value])
