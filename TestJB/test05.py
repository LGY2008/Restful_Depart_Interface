from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
url="file:///E:/%E8%AF%BE%E5%A0%82/WebDriver/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)
username=driver.find_element_by_xpath("//*[@id='userA']")
# username.send_keys("admin")
print("元素为：",username)
ActionChains(driver).context_click(username).perform()
username.send_keys('p')
# username.send_keys("alt")
sleep(3)
driver.close()