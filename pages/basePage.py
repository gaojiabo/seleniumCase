# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : basePage.py
# @ide     : PyCharm
# @time    : 2020/12/23 21:04
from myDriverTool.myDriver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.mySettings import time_out, poll_time


class BasePage:
    """
    basepage 是将一些页面通用的方法，抽离出来封装起来
    """
    def __init__(self):
        # 获取浏览器驱动对象
        self.driver = Driver.get_driver("Chrome")

    def get_element(self, locator):
        """
        显示等待，查找元素
        :param locator: 要求传入的参数是一个元组，表示元素定位方法和表达式
        :return: 单个的元素对象
        """
        WebDriverWait(
            # 传入浏览器对象
            driver=self.driver,
            # 传入超时时间
            timeout=time_out,
            # 设置轮询时间
            poll_frequency=poll_time).until(
            EC.visibility_of_element_located(locator)
        )

        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        """
        显示等待，查找元素
        :param locator: 要求传入的参数是一个元组，表示元素定位方法和表达式
        :return: 元素列表
        """
        WebDriverWait(
            # 传入浏览器对象
            driver=self.driver,
            # 传入超时时间
            timeout=time_out,
            # 设置轮询时间
            poll_frequency=poll_time).until(
            EC.visibility_of_element_located(locator)
        )

        return self.driver.find_elements(*locator)
