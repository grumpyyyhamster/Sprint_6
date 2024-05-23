from selenium.webdriver.common.by import By


class OrderScooterPageLocators:
    # локаторы полей ввода данных на странице "Для кого самокат"
    NAME = By.XPATH, "//input[@placeholder='* Имя']"
    SURNAME = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    SUBWAY_STATION = By.XPATH, "//input[@placeholder='* Станция метро']"
    SUB_STATION_USERS = {
        1: [By.XPATH, ".//div[text()='Славянский бульвар']"],
        2: [By.XPATH, ".//div[text()='Крылатское']"]
    }
    PHONE = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, "//button[text()='Далее']"

    # локаторы полей ввода данных на странице "Про аренду"
    DATE = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    NUMBER_OF_DATE = {
        1: [By.XPATH, "// div[text() = '23']"],
        2: [By.XPATH, "// div[text() = '25']"]
    }
    RENTAL_USER_FIELD = By.XPATH, "//div[text()='* Срок аренды']"
    RENTAL_USER = {
        1: [By.XPATH, "//div[text()='двое суток']"],
        2: [By.XPATH, "//div[text()='трое суток']"]
    }
    COLOR_USER = {
        1: [By.XPATH, "//input[@id='black']"],
        2: [By.XPATH, "//input[@id='grey']"]
    }
    COMMENT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"

    ORDER_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"  # кнопка заказа самоката
    CONFIRM = By.XPATH, "//button[text()='Да']"  # кнопка подтверждения заказа
    ORDER_CONFIRMED_BUTTON = By.XPATH, "//button[text()='Посмотреть статус']"  # Кнопка "Посмотреть статус"

    DZEN_LOGO = By.XPATH, "//div[contains(@class, 'desktop-base-header__logoContainer-3l desktop-base-header__isMorda-mX')]"  # лого Яндекс.Дзен
