# coding=utf-8

from selenium import webdriver


browser = webdriver.Chrome()
browser.get(constants.linkedin_url)
print("You are in Linkedin !")
