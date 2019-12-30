# coding=utf-8

from selenium import webdriver
import time
import user_iterations
import constants

browser = webdriver.Chrome()
browser.get(constants.linkedin_url)
print("You are in Linkedin !")
time.sleep(3)

try:

    login_button = browser.find_element_by_xpath(constants.login_button_xpath)
    login_button.click()
    print("You can see Login Page. ")

    time.sleep(3)

    username = browser.find_element_by_xpath(constants.username_input_text_xpath)
    password = browser.find_element_by_xpath(constants.password_input_text_xpath)

    username.send_keys(user_iterations.your_username)
    password.send_keys(user_iterations.your_password)
    print("You can see your account info written.")

    time.sleep(3)

    login = browser.find_element_by_xpath(constants.press_login_button_xpath)
    login.click()
    print("You can Logged In ! You can see your dashboard.")

    time.sleep(3)

    messages = browser.find_element_by_xpath(constants.messages_in_dashboard_xpath)
    messages.click()
    print("You can see Your Message Page.")

    time.sleep(3)

    new_messages = browser.find_element_by_xpath(constants.new_message_button_xpath)
    new_messages.click()
    print("You can see Login Page.")

    time.sleep(4)

    message_for_who = browser.find_element_by_class_name(constants.message_for_who_input_text)
    message_for_who.send_keys(user_iterations.person_you_want_to_send_message)
    print("You can write the person who want to send a message.")

    time.sleep(4)

    message_text = browser.find_element_by_css_selector(constants.message_text_css_selector)
    message_text.send_keys(user_iterations.message_you_want_to_send)
    print("You can see your message.")

    print("Browser will close in 10 seconds")
    time.sleep(10)
    browser.close()

except Exception as error:
    browser.close()
    print("There is an error :", error.message)