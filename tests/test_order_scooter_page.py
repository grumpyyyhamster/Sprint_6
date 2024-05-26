import allure
import pytest
from conftest import driver
from data_to_use import TestData
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from pages.order_scooter_page import OrderScooterPage


class TestRedirect:
    @allure.title('Тест на проверку редиректа на хоум страницу при нажатии на лого Самокат')
    def test_redirect_scooter_logo_successefull(self, driver):
        osp = OrderScooterPage(driver)
        osp.click_on_scooter_logo()
        current_url = osp.get_url_dzen()
        assert current_url == TestData.HOME_URL

    @allure.title('Тест на проверку редиректа на Дзен страницу при нажатии на лого Яндекс')
    def test_redirect_yandex_logo_successefull(self, driver):
        osp = OrderScooterPage(driver)
        osp.click_on_yandex_logo()
        osp.switch_to_new_tab_dzen()
        osp.waiting_page_dzen_logo()
        current_url = osp.get_url_dzen()
        assert current_url == TestData.DZEN_URL


class TestOrders:

    @allure.title('Набор тестов, проверяющих успешное оформление заказа при нажатии на кнопки Заказать (в разных локациях)')
    @pytest.mark.parametrize('button, reg_data_user_part1, reg_data_user_part2, number_of_user',
                             [(HomePageLocators.HEADER_ORDER_BUTTON, TestData.REG_DATA_USER1_1,
                               TestData.REG_DATA_USER1_2, 1),
                              (HomePageLocators.ORDER_BUTTON, TestData.REG_DATA_USER2_1, TestData.REG_DATA_USER2_2, 2)])
    def test_order_successefull(self, driver, button, reg_data_user_part1, reg_data_user_part2, number_of_user):
        osp = OrderScooterPage(driver)
        osp.scroll_to_item(button)
        osp.click_on_item(button)
        osp.setup_first_data(reg_data_user_part1, number_of_user)
        osp.setup_second_data(reg_data_user_part2, number_of_user)
        result = osp.checking_if_order_is_successful()
        assert result == 'Посмотреть статус'
