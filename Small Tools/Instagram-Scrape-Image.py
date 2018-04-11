from selenium import webdriver
from time import sleep
from urllib import urlretrieve

driver = webdriver.Chrome('/home/coderpham/chromedriver')		# <--- Need to download chromedriver and put its path here
driver.get('https://www.instagram.com/accounts/login/?hl=vi')	# <--- Login page in VNese

usr = driver.find_element_by_name('username')
usr.send_keys('foo@gmail.com')									# <--- Put your username 

pwd = driver.find_element_by_name('password')
pwd.send_keys('abcd')											# <--- Put your password here

sign_in = driver.find_element_by_tag_name('button')
sign_in.click()

driver.get('https://www.instagram.com/.....')					# <--- Put instagram page which you need to scrape 

posts = driver.find_element_by_class_name('_fd86t')
if ',' in posts.text:
    posts = posts.text
    posts = posts.replace(',','')
posts = int(posts)

images_url = []

# for infinite scrolling page
for i in range(0,posts/12 + 1):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    sleep(1)
    images = driver.find_elements_by_tag_name('img')
    images = [img.get_attribute('src') for img in images]
    images_url = images_url + images
    sleep(1)
    images_url = list(set(images_url))      #Cut down all duplicate links
    
# Download all images url it can find and put in the same path of this python file	
count = 1
for url in images_url:
    urlretrieve(url, str(count) + '.jpg')
    count = count + 1
