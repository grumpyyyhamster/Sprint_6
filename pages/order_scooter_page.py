import allure

from locators.home_page_locators import HomePageLocators
from locators.order_scooter_page_locators import OrderScooterPageLocators
from pages.base_page import BasePage


class OrderScooterPage(BasePage):

    @allure.step('Заполнение первой формы и переход ко второй')
    def setup_first_data(self, reg_data_values, number_of_user):
        self.click_on_item(OrderScooterPageLocators.NAME)
        self.set_value_for_input(OrderScooterPageLocators.NAME, reg_data_values[0])
        self.click_on_item(OrderScooterPageLocators.SURNAME)
        self.set_value_for_input(OrderScooterPageLocators.SURNAME, reg_data_values[1])
        self.click_on_item(OrderScooterPageLocators.ADDRESS)
        self.set_value_for_input(OrderScooterPageLocators.ADDRESS, reg_data_values[2])
        self.click_on_item(OrderScooterPageLocators.SUBWAY_STATION)
        self.set_value_for_input(OrderScooterPageLocators.SUBWAY_STATION, reg_data_values[3])
        self.click_on_item(OrderScooterPageLocators.SUB_STATION_USERS[number_of_user])
        self.waiting_for_item_to_be_visible(OrderScooterPageLocators.PHONE)
        self.click_on_item(OrderScooterPageLocators.PHONE)
        self.set_value_for_input(OrderScooterPageLocators.PHONE, reg_data_values[4])
        self.click_on_item(OrderScooterPageLocators.COOKIE_BUTTON)
        self.scroll_to_item(OrderScooterPageLocators.NEXT_BUTTON)
        self.click_on_item(OrderScooterPageLocators.NEXT_BUTTON)

    @allure.step('Заполнение второй формы и подтверждение')
    def setup_second_data(self, reg_data_values_2, number_of_user):
        self.waiting_for_item_to_be_visible(OrderScooterPageLocators.DATE)
        self.click_on_item(OrderScooterPageLocators.DATE)
        self.set_value_for_input(OrderScooterPageLocators.DATE, reg_data_values_2[0])
        self.click_on_item(OrderScooterPageLocators.NUMBER_OF_DATE[number_of_user])
        self.waiting_for_item_to_be_visible(OrderScooterPageLocators.RENTAL_USER_FIELD)
        self.click_on_item(OrderScooterPageLocators.RENTAL_USER_FIELD)
        self.click_on_item(OrderScooterPageLocators.RENTAL_USER[number_of_user])
        self.click_on_item(OrderScooterPageLocators.COLOR_USER[number_of_user])
        self.click_on_item(OrderScooterPageLocators.COMMENT)
        self.set_value_for_input(OrderScooterPageLocators.COMMENT, reg_data_values_2[1])
        self.scroll_to_item(OrderScooterPageLocators.ORDER_BUTTON)
        self.click_on_item(OrderScooterPageLocators.ORDER_BUTTON)
        self.waiting_for_item_to_be_visible(OrderScooterPageLocators.CONFIRM)
        self.click_on_item(OrderScooterPageLocators.CONFIRM)

    @allure.step('Проверка успешности оформления заказа')
    def checking_if_order_is_successful(self):
        self.waiting_for_item_to_be_visible(OrderScooterPageLocators.ORDER_CONFIRMED_BUTTON)
        return self.item_text(OrderScooterPageLocators.ORDER_CONFIRMED_BUTTON)

    @allure.step('Ожидание отображения лого Дзен на странице')
    def waiting_page_dzen_logo(self):
        self.waiting_for_item_to_be_visible(OrderScooterPageLocators.DZEN_LOGO)

    @allure.step('Переход на новую вкладку Дзен')
    def switch_to_new_tab_dzen(self):
        self.switch_to_new_tab()

    @allure.step('Получение URL Дзен')
    def get_url_dzen(self):
        self.get_url()

    @allure.step('Кликнуть на лого "Самокат"')
    def click_on_scooter_logo(self):
        self.click_on_item(OrderScooterPageLocators.LOGO2)

    @allure.step('Кликнуть на лого "Яндекс"')
    def click_on_yandex_logo(self):
        self.click_on_item(OrderScooterPageLocators.LOGO1)
