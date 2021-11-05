from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\\Users\\micha\\OneDrive\\Desktop\\Other\\chromedriver.exe"

chrome = webdriver.Chrome(PATH)


def to_website(link):
    chrome.get(link)


def find_el(method, content):
    if method == "xpath":
        output = chrome.find_element_by_xpath(content)
    elif method == "id":
        output = chrome.find_element_by_id(content)
    elif method == "class":
        output = chrome.find_element_by_class_name(content)
    elif method == "name":
        output = chrome.find_element_by_name(content)
    else:
        print("Sorry, unknown means of access.")
    return output


to_website("https://clockify.me")
