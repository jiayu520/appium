# -*- coding: utf-8 -*-
from appium import webdriver
desired_caps={}
desired_caps['platformName']='Android'#测试平台
desired_caps['platformVersion']='6.0.1'#测试版本
desired_caps['deviceName']='127.0.0.1:7555'#测试设备
desired_caps['appPackage']='com.android.settings'#被测包名
desired_caps['appActivity']='com.android.settings.Settings'#被测页面，一般是欢迎页或者首页，Android是有页面和包的区分的
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.quit()
