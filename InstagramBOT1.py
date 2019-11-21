from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


def login():
	username="YourUserName"
	password="YourPassWord"
	time.sleep(1)
	username=browser.find_element_by_name('username')
	username.send_keys(username)
	
	passw=browser.find_element_by_name('password')
	passw.send_keys(password)
	print('login done')
	browser.find_element_by_xpath("/html/body/span/section/main/div/article/div/div[1]/div/form/div[4]").click()



def noticlose():
	try:
		browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
	except NoSuchElementException:
		print("in try")
		time.sleep(1)
		noticlose()

def putlike():
	a=["chennai"]
	for k in a:
		browser.get('https://www.instagram.com/explore/tags/'+k+'/')
		browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]').click()
		print('tag done')
		time.sleep(2)
		for i in range(3):
			browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
			browser.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/a[2]").click()
			time.sleep(2)


browser=webdriver.Chrome()
web="https://www.instagram.com/accounts/login/?source=auth_switcher"
browser.get(web)
print('in')

login()
noticlose()
print("notidone")
time.sleep(2)
putlike()