from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import email
import smtplib



browser = webdriver.Chrome("/usr/local/bin/chromedriver")
browser.get("https://de.louisvuitton.com/deu-de/produkte/nano-noe-monogram-010573")
time.sleep(5) 
if "<span id=\"priceBtnMsg\" class=\"contact-description\" style=\"\">Das Produkt ist derzeit nicht verfügbar</span>" in browser.page_source:
	print("NO")
browser.quit()