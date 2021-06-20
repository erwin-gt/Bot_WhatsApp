from selenium import webdriver
import time
import os, time

driver = webdriver.Chrome(executable_path=r"C:\Users\Erwin\Documents\GitHub\Bot_WhatsApp\chromedriver.exe")

driver.get("https://www.python.org")
time.sleep(10)

driver.close()

