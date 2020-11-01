import logging
import os
import playwright


name_entry = '1@mail.com'
pwd_entry = '@#^0'


FBcode000 = str('https://www.facebook.com/')

FBcode010 = str('//*[@id="email"]')
FBcode011 = str('//*[@id="pass"]')
FBcode012 = str('//*[@id="u_0_b"]')


def fblogin(page):
	page.goto(FBcode000)
	page.fill(FBcode010, name_entry)
	page.fill(FBcode011, pwd_entry)
	page.click(FBcode012)
	os.system("pause")




if __name__ == "__main__":
	playwr = playwright.sync_playwright().start()
	browser = playwr.chromium.launch(headless=False)
	page = browser.newPage()
	try:
		fblogin(page)
	except Exception as e:
		logging.exception(e)
	finally:
		browser.close()
		playwr.stop()
