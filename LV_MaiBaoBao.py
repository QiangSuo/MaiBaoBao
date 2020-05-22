from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import email
import smtplib
from email.mime.text import MIMEText
import datetime
import time
from selenium.webdriver.chrome.options import Options


def BaoBaoYouHuo(url,timeToSleep):
	#CHROME_PATH = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	#chrome_options = Options()  
	#chrome_options.headless = True
	#chrome_options.binary_location = CHROME_PATH
	#browser = webdriver.Chrome("chromedriver", options=chrome_options)
	browser = webdriver.Chrome("chromedriver")  
	browser.set_window_size(2000, 1000)
	browser.get(url)
	time.sleep(timeToSleep) 
	if "Nicht verfügbar?  Besuchen Sie uns bald wieder!" in browser.page_source and "Zur Auswahl hinzufügen" not in browser.page_source:
		browser.quit()
		return False
	elif "Zur Auswahl hinzufügen" in browser.page_source and "<span id=\"priceBtnMsg\" class=\"contact-description\" style=\"\">Das Produkt ist derzeit nicht verfügbar</span>" not in browser.page_source:
		#imageName ="C:\\Users\\mv-adm-Qiang\\Desktop\\Log\\" + str(datetime.datetime.now())[0:22].replace(".","-").replace(":","-") + ".png"
		#browser.get_screenshot_as_file(imageName) 
		browser.quit()
		return True
	else:
		print("Here")
		browser.quit()

timeToSleep = 5
BaoBaoList = ["https://de.louisvuitton.com/deu-de/produkte/nano-noe-monogram-010573",
"https://de.louisvuitton.com/deu-de/produkte/multi-pochette-accessoires-monogram-nvprod1770359v",
"https://de.louisvuitton.com/deu-de/produkte/multi-pochette-accessoires-monogram-nvprod1770359v#M44840",
"https://de.louisvuitton.com/deu-de/produkte/pochette-metis-monogram-reverse-canvas-nvprod1770373v",
"https://de.louisvuitton.com/deu-de/produkte/palm-springs-mini-monogram-reverse-canvas-nvprod1770369v",
"https://de.louisvuitton.com/deu-de/produkte/nano-speedy-monogram-010575",
"https://de.louisvuitton.com/deu-de/produkte/mini-pochette-accessoires-monogram-001025",
"https://de.louisvuitton.com/deu-de/produkte/favorite-mm-monogram-005658",
"https://de.louisvuitton.com/deu-de/produkte/mini-pochette-accessoires-monogram-001025",
"https://de.louisvuitton.com/deu-de/produkte/mini-pochette-accessoires-damier-azur-001034",
"https://de.louisvuitton.com/deu-de/produkte/mini-pochette-accessoires-damier-ebene-001035"]

fromMail = "testFrom@mail.com"
psw = "Password"
ToMail = "testTo@mail.com"

#countRunTimes = 0

while True:
	for BaoBao in BaoBaoList:
		try:
			if BaoBaoYouHuo(BaoBao,timeToSleep):
				msg = email.message_from_string("有货")
				msg = MIMEText(BaoBao, 'plain', 'utf-8')
				msg['From'] = fromMail
				msg['To'] = ToMail
				msg['Subject'] = "有货了老婆,冲鸭!!!"
				s = smtplib.SMTP("smtp.live.com",587) # Hotmail
				s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
				s.starttls() #Puts connection to SMTP server in TLS mode
				s.ehlo()
				s.login(fromMail, psw)
				s.sendmail(fromMail, ToMail, msg.as_string())
				s.quit()
			else:
				pass
		except Exception:
			pass
		else:
			pass
	time.sleep(1)
#	countRunTimes = countRunTimes+1
#	text_file = open("C:\\Users\\mv-adm-Qiang\\Desktop\\log\\Log.txt", "a")
#	text_file.write("\n" + 'RunTime: ' + str(countRunTimes) + ' at ' + str(datetime.datetime.now()))
#	text_file.close()




