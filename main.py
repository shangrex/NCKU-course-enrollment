import time
from selenium import webdriver
from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import pandas as pd
import logging
import csv
import argparse
import logging

parser = argparse.ArgumentParser()

#url = parser.add_argument("--NCKU url", type=str, required=True)
main_page_url = "https://course.ncku.edu.tw/index.php"


student_id = parser.add_argument("--sid", type=str, required=True, 
                                default="F74072138")

student_psd = parser.add_argument("--psd", type=str, required=True,
                                default="none")


browser = webdriver.Chrome()
browser.get(main_page_url)

log_url = browser.find_element_by_class_name("dsp").get_attribute("href")

browser.get(log_url)

student_id_button = browser.find_element_by_class_name("rwd_input1_6 rwd_input1_7")

student_pad_button = browser.find_element_by_class_name("rwd_input1_6 rwd_input1_7")

verify_button = browser.find_element_by_id("code")


# soup = BeautifulSoup(browser.page_source)
# goal = soup.find_all("href")
# print(goal)

