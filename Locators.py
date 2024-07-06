from selenium.webdriver.common.by import By
from BasePage import BasePage

class locators():

    def text_input_word(self):
        return "//*[contains(@class, 'home')]//*[text() = 'Text input']"

    def input_text(text):
        return f"//*[text() = '{text}']//ancestor-or-self::*[contains(@id, 'user') and contains (@id, 'wrapper')]//input"

    def textarea_text(text):
        return f"//*[text() = '{text}']//ancestor-or-self::*[contains(@id, 'Address-wrapper')]//textarea"

    def checkBox(text):
        return f"//*[text() = '{text}']"


class PageObject(BasePage):

    def click_input_word(self):
        button = self.find_presence_element(locator=(By.XPATH, locators.text_input_word))
        button.click()