import time
from selenium import webdriver
from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import pandas as pd
import logging
import csv
import argparse
import logging
import subprocess
from PIL import Image

parser = argparse.ArgumentParser()

#url = parser.add_argument("--NCKU url", type=str, required=True)
main_page_url = "https://course.ncku.edu.tw/index.php"


parser.add_argument("--sid", type=str, default="F74072138")

parser.add_argument("--psd", type=str, default="none")
args = parser.parse_args()

browser = webdriver.Chrome()
browser.get(main_page_url)

log_url = browser.find_element_by_class_name("dsp").get_attribute("href")

browser.get(log_url)

'''
print(args.sid)
print(args.psd)
'''
browser.find_element_by_id("user_id").send_keys(args.sid)

browser.find_element_by_id("passwd").send_keys(args.psd)

img = browser.find_element_by_xpath("//img[@class='click']")
browser.save_screenshot('test.jpg')
img = Image.open('test.jpg')
img = img.crop((910, 622, 980, 650))
img.save('img.png', 'png')
ocr = subprocess.Popen("tesseract /img.png /result")
ocr.wait()
text = open("/result.txt").read().strip()

browser.find_element_by_id("code").send_keys(text)

browser.find_element_by_css_selector("#submit_by_acpw > span").click()

# soup = BeautifulSoup(browser.page_source)
# goal = soup.find_all("href")
# print(goal)

