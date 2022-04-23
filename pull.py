from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import requests
import os
from urllib.request import urlretrieve
chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
if not os.path.exists('output'):
    os.mkdir('output')
def scrolling():
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
driver.get("https://images.google.com/")
keyword=input("enter the keyword please")
search=driver.find_element_by_xpath("//input[@aria-label='Search']")
search.send_keys(f"{keyword} imagesize:480x320")
search.send_keys(Keys.ENTER)
scrolling()
images=driver.find_elements_by_xpath("//div[@jsname='DeysSe']")
p=1
for i in images:
    i.send_keys(Keys.ENTER)
    time.sleep(1)
    image_link = driver.find_element_by_css_selector("#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id > div > a > img").get_attribute("src")
    response=requests.get(image_link)
    try:
        from bs4 import BeautifulSoup
        soup=BeautifulSoup(response.text,"html.parser")
        urlretrieve(image_link,f"output/{p}.png")
        p+=1
    except:
        pass
            
