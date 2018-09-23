import collections
import os
import re
from getpass import getpass
from time import sleep
from urllib.request import urlretrieve

from colorama import Fore, Style, init

from selenium import webdriver

init()


def story_download(url, driver):
    '''STORY_DOWNLOAD
    Arguments:
        url {String} -- URL of stories
        driver {webdriver} -- Current webdriver

    Return:
        stories {list} -- List of stories's url
    '''
    stories = []
    while driver.current_url == url:
        sleep(1)
        try:
            story = driver.find_element_by_xpath("//div[@class='qbCDp']")
        except:
            break
        try:
            stories.append(story.find_element_by_tag_name(
                'source').get_attribute('src'))
        except:
            try:
                stories.append(story.find_element_by_tag_name(
                    'img').get_attribute('src'))
            except:
                pass
    stories = list(collections.OrderedDict.fromkeys(stories))
    return stories

os.system('cls')
print(Fore.CYAN + '''
 _____          _                                    _____
|_   _|        | |                                  /  ___|
  | | _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   \ `--.  ___ _ __ __ _ _ __   ___ _ __
  | || '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \   `--. \/ __| '__/ _` | '_ \ / _ \ '__|
 _| || | | \__ \ || (_| | (_| | | | (_| | | | | | | /\__/ / (__| | | (_| | |_) |  __/ |
 \___/_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| \____/ \___|_|  \__,_| .__/ \___|_|
                          __/ |                                          | |
                         |___/                                           |_|              ''')

print(Fore.LIGHTBLUE_EX + "Dev by Coder-Pham\n".center(os.get_terminal_size().columns))
print(Style.RESET_ALL)
print(Fore.LIGHTRED_EX + '{:^35s}'.format("Option for your browser:"))
print(Fore.LIGHTRED_EX + '{:>18s}'.format("1. Chrome"))
print(Fore.LIGHTRED_EX + '{:>20s}'.format("2. Firefox\n"))
browser = input('{:>18s}'.format("Your option: "))
print(Style.RESET_ALL)
username = input('{:>15s}'.format("Username: "))
password = getpass(prompt='{:>15s}'.format("Password: "))
print()
url = input('{:>24s}'.format('Instagram profile: '))

# Login
if browser.upper() == "CHROME":
    driver = webdriver.Chrome('chromedriver.exe')
else:
    driver = webdriver.Firefox('geckodriver.exe')

driver.get('https://www.instagram.com/accounts/login')
sleep(1.5)

usr = driver.find_element_by_name('username')
usr.send_keys(username)
pwd = driver.find_element_by_name('password')
pwd.send_keys(password)

sign_in = driver.find_element_by_tag_name('button')
sign_in.click()
sleep(1.5)

if not driver.current_url == 'https://www.instagram.com':
    print(Fore.LIGHTRED_EX +
          'Login takes too much time. Try again with more decent Internet')
    print(Style.RESET_ALL)
    driver.quit()
    exit()
else:
    driver.get(url)

posts = driver.find_element_by_class_name('g47SY ')
posts = posts.text
if ',' in posts:
    posts = posts.replace(',', '')
scroll = int(int(posts)/12 + 1)
print("Found {} Instagram objects".format(posts))
print("Start fetching url...")
print()

images_url = []
videos_url = []
stories_preview = re.compile(r'^((?!(/s150x150/)).)*$')

# for infinite scrolling page
clickable_object = []
for i in range(scroll):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    sleep(1)
    # ! Parent path of every Object
    # @param group_of_12 - Every time scroll, Instagram response back max 12 objects
    clickable_object = driver.find_elements_by_xpath(
        "//div[@class='v1Nh3 kIKUG  _bz0w']")

    for Insta_Obj in clickable_object:
        # Just get image. Even preview image of video
        try:
            images_url.append(Insta_Obj.find_element_by_tag_name(
                'img').get_attribute('src'))
        except:
            print(Fore.RED + "1 Error have been handling.")
        try:
            # Get album of images
            if Insta_Obj.find_element_by_class_name('coreSpriteSidecarIconLarge ').text == 'Post':
                Insta_Obj.click()
                sleep(1)
                # ? How to avoid get preview of stories (by find /s150x150/ in url)
                while True:
                    try:
                        album = driver.find_elements_by_xpath(
                            "//li[@class='_-1_m6']")
                        for image in album:
                            # In Posts can have video
                            try:
                                videos_url.append(image.find_element_by_tag_name(
                                    'video').get_attribute('src'))
                            except:
                                try:
                                    images_url.append(image.find_element_by_tag_name(
                                        'img').get_attribute('src'))
                                    # Exclude preview images from saved stories
                                    if stories_preview.search(images_url[-1]) == None:
                                        images_url.pop()
                                except:
                                    # In Posts, after swipe right, the previous image will be deprecated
                                    pass
                        # Swipe right to get all album src
                        driver.find_element_by_xpath(
                            "//div[@class='    coreSpriteRightChevron']").click()
                        sleep(0.5)
                    except:
                        # End of album will no more Swipe button
                        break
                sleep(0.5)
                driver.find_element_by_class_name("ckWGn").click()
        except:
            try:
                # Get videos
                if Insta_Obj.find_element_by_class_name('coreSpriteVideoIconLarge ').text == 'Video':
                    images_url.pop()    # Because just push preview image of video early on
                    Insta_Obj.click()
                    # TODO: How to get correct video
                    sleep(1)
                    videos_url.append(driver.find_element_by_tag_name(
                        'video').get_attribute('src'))
                    driver.find_element_by_class_name("ckWGn").click()
            except:
                pass

images_url = list(collections.OrderedDict.fromkeys(images_url))
videos_url = list(collections.OrderedDict.fromkeys(videos_url))

print(Style.RESET_ALL)
print("Start downloading...")
# Download all images url it can find and put in the same path of this python file
if not os.path.isdir("Image"):
    os.makedirs("Image")
    count = 1
    for image_url in images_url:
        urlretrieve(image_url, os.path.join("Image", str(count) + '.jpg'))
        count = count + 1

# Download all videos
if (not os.path.isdir("Video")) and (not videos_url == []):
    os.makedirs("Video")
    count = 1
    for video_url in videos_url:
        urlretrieve(video_url, os.path.join("Video", str(count) + ".mp4"))
        count = count + 1

# Download all stories
try:
    driver.get(url.replace('.com/', '.com/stories/'))
except:
    pass
else:
    if not os.path.isabs("Stories"):
        os.makedirs("Stories")
    stories = story_download(url.replace('.com/', '.com/stories/'), driver)
    count = 1
    for story_url in stories:
        file_type = story_url.split('.')[-1]
        urlretrieve(story_url, os.path.join(
            "Stories", str(count) + '.' + file_type))
        count = count + 1

driver.quit()
print("Done")
