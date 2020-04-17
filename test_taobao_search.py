# -*- coding: utf-8 -*-
from appium import webdriver
desired_caps={
  "platformName": "Android",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.taobao.taobao",
  "appActivity": "com.taobao.tao.TBMainActivity"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(10)
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout")
el1.click()
el2 = driver.find_element_by_id("com.taobao.taobao:id/searchEdit")
el2.send_keys("冰箱")
el3 = driver.find_element_by_accessibility_id("搜索")
el3.click()
