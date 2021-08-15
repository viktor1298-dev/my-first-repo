from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time

# 1

my_driver = webdriver.Chrome(executable_path="C:/Users/ViKToR/Desktop/chromedriver.exe")
# my_driver.get("http://www.walla.co.il")
# my_firefox = webdriver.Firefox(executable_path="C:/Users/ViKToR/Desktop/geckodriver.exe")
# my_firefox.get("http://www.ynet.co.il")

# 2

# get_title = my_driver.title
# my_driver.refresh()
# if get_title == my_driver.title:
#     print("equal")
# else:
#     print("not the same title")

# 3 - Yes

# 4


my_driver.get("https://translate.google.com/")

my_driver.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz["
                                "1]/span/span/div/textarea").send_keys("בדיקה אחת שתיים")
time.sleep(2)

# 5

my_driver.execute_script("window.open('http://www.youtube.com')")
my_driver.switch_to.window(my_driver.window_handles[1])
my_driver.find_element_by_name("search_query").send_keys("rickrolled")
my_driver.find_element_by_name("search_query").submit()
time.sleep(2)

# 6

my_driver.execute_script("window.open('https://translate.google.com')")
my_driver.switch_to.window(my_driver.window_handles[2])
my_driver.find_element_by_class_name("er8xn").send_keys("hello1 ")
my_driver.find_element_by_tag_name("textarea").send_keys("hello2 ")
my_driver.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz["
                                "1]/span/span/div/textarea").send_keys("hello3")

time.sleep(2)

# 7

my_driver.execute_script("window.open('https://www.facebook.com')")
my_driver.switch_to.window(my_driver.window_handles[3])
my_driver.find_element_by_id("email").send_keys("viktor@yahoo.com")
my_driver.find_element_by_id("pass").send_keys("password")
my_driver.find_element_by_name("login").click()
time.sleep(2)

# CHALLENGE

#  8
my_driver.execute_script("window.open('https://www.facebook.com')")
my_driver.switch_to.window(my_driver.window_handles[4])
print(my_driver.get_cookies())
my_driver.delete_all_cookies()
print(my_driver.get_cookies())
time.sleep(2)

#  9

my_driver.execute_script("window.open('https://github.com')")
my_driver.switch_to.window(my_driver.window_handles[5])
my_driver.find_element_by_name("q").send_keys("Selenium" + Keys.ENTER)

# 10

Options.add_argument("--disable-extensions")





