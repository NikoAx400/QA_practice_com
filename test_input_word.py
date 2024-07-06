from Locators import PageObject
import pytest
from confest import browser
import time



def test_input_word(browser):
    qapractice = PageObject(browser)
    time.sleep(2)
    qapractice.click_input_word()
    time.sleep(2)

