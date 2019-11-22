from selenium import webdriver
import time

def logg():
	username="YourUserName"
	password="YourPassword"
	browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username)
	browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
	browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()

def noti():
	browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()

def likes():
	hashtag=["programming","java"]
	for k in hashtag:

		browser.get('https://www.instagram.com/explore/tags/'+k+'/')
		try:

			browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]').click()
		except:
			time.sleep(5)
			browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]').click()
		for i in range(20):
			time.sleep(2)
			try:
				browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
				
				browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
				
				browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a[2]').click()
			except:
				try:
					browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
				except:
					browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button[2]').click()
				browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a[2]').click()
			





browser = webdriver.Chrome()
browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
time.sleep(2)
logg()
time.sleep(2)
noti()
time.sleep(2)
likes()

browser.close()