#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver

class Driver():

    def __init__(self):
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "192.168.8.100:62001",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": ".main.MainActivity",
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }
        self.server = 'http://127.0.0.1:4723/wd/hub'
        self.driver = webdriver.Remote(self.server, self.desired_caps)

if __name__ == '__main__':
    action = Driver()

