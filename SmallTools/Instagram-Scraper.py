from selenium import webdriver
from time import sleep
from urllib import urlretrieve
import argparse
import os

parser = argparse.ArgumentParser(prog='Instagram Scraper v1.0', usage='Use -h for help')
parser.add_argument('-p', '--path', dest='path', default='/home/chromedriver', help='Chromedriver path for execute program')
parser.add_argument('-u', '--username', dest='username', default='', help='Your Instagram username')
parser.add_argument('-w', '--password', dest='password', default='', help='Your Instagram password')
parser.add_argument('-l', '--urllink', dest='url', help='Instagram url link you want to scrape')

args = parser.parse_args()

while not os.path.exists(args.path):
    args.path = raw_input('Please fill path for chromedriver: ')
driver = webdriver.Chrome(args.path)		# <--- Need to download chromedriver and put its path here
driver.get('https://www.instagram.com/accounts/login/?hl=vi')
sleep(1)

usr = driver.find_element_by_name('username')
while args.username == '':
    args.username = raw_input('Please fill your username: ')
usr.send_keys(args.username)									# <--- Put your username

pwd = driver.find_element_by_name('password')
while args.password == '':
    args.password = raw_input('Please fill your password: ')
pwd.send_keys(args.password)											# <--- Put your password here

sign_in = driver.find_element_by_tag_name('button')
sign_in.click()
sleep(1)

if args.url is None:
    print "No Instagram profile found"
    exit()

driver.get(args.url)					# <--- Put instagram page which you need to scrape

posts = driver.find_element_by_class_name('_fd86t')
posts = posts.text
if ',' in posts:
    posts = posts.replace(',', '')
posts = int(posts)

images_url = []

# for infinite scrolling page
for i in range(0, posts/12 + 1):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    sleep(1)
    images = driver.find_elements_by_tag_name('img')
    images = [img.get_attribute('src') for img in images]
    images_url = images_url + images
    sleep(1)
    images_url = list(set(images_url))      # Cut down all duplicate links

# Download all images url it can find and put in the same path of this python file
count = 1
for url in images_url:
    urlretrieve(url, str(count) + '.jpg')
    count = count + 1

driver.quit()
