# coding=utf-8
# myDriver
# 2020/12/25
from selenium import webdriver
from utils.mySettings import url

class Driver:
    '''浏览器工具类'''
    #'''初始化一个为none的driver'''
    _driver = None #给子类使用的加一个下划线,习惯而已，没有什么语法意义

    @classmethod #不需要实例化就能使用的方法节省空间
    def get_driver(cls,brower_name="Chrome"):
        '''
        获取浏览器驱动对象
        :param brower_name: 浏览器类型
        :return: 返回一个driver浏览器驱动对象
        '''
        #判断是否为空
        if cls._driver is None:
            if brower_name == 'Chrome':
                cls._driver = webdriver.Chrome()
            elif brower_name == 'Firefox':
                cls._driver = webdriver.Firefox()
            #最大化窗口操作
            cls._driver.maximize_window()
            #访问默认网页
            cls._driver.get(url)
            #执行登陆
            cls.__login()
        return cls._driver

    @classmethod
    def __login(cls): #私有函数不会污染外部空间
        '''
        私有方法，只能在类里面使用
        类外部无法使用，子类也无法继承
        只在浏览器打开的时候执行一次登陆
        :param cls:
        :return:
        '''
        cls._driver.find_element_by_name('username').send_keys('libai')
        cls._driver.find_element_by_name('password').send_keys('opmsopms123')
        cls._driver.find_element_by_css_selector('button').click()

if __name__ == '__main__':
    #如果需要等待就调用我们自己
    Driver.get_driver()












