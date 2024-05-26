from selenium.webdriver.common.by import By


class HomePageLocators:
    # список вопросов
    QUESTIONS = {
        1: [By.XPATH, "//div[@id='accordion__heading-0']"],
        2: [By.XPATH, "//div[@id='accordion__heading-1']"],
        3: [By.XPATH, "//div[@id='accordion__heading-2']"],
        4: [By.XPATH, "//div[@id='accordion__heading-3']"],
        5: [By.XPATH, "//div[@id='accordion__heading-4']"],
        6: [By.XPATH, "//div[@id='accordion__heading-5']"],
        7: [By.XPATH, "//div[@id='accordion__heading-6']"],
        8: [By.XPATH, "//div[@id='accordion__heading-7']"]
    }

    # список ответов
    ANSWERS = {
        1: [By.XPATH, "//div[@id='accordion__panel-0']"],
        2: [By.XPATH, "//div[@id='accordion__panel-1']"],
        3: [By.XPATH, "//div[@id='accordion__panel-2']"],
        4: [By.XPATH, "//div[@id='accordion__panel-3']"],
        5: [By.XPATH, "//div[@id='accordion__panel-4']"],
        6: [By.XPATH, "//div[@id='accordion__panel-5']"],
        7: [By.XPATH, "//div[@id='accordion__panel-6']"],
        8: [By.XPATH, "//div[@id='accordion__panel-7']"]
    }

    FAQ_SECTION = By.XPATH, "//div[text()='Вопросы о важном']"  # секция страницы с вопросами

    # кнопки заказов в хедере и на хоум странице
    HEADER_ORDER_BUTTON = By.XPATH, "//div[@class = 'Header_Nav__AGCXC']/button[@class='Button_Button__ra12g']"
    ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button"
