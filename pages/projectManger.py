# coding=utf-8
# projectManger--项目管理页面类
# 2020/12/25
from pages.basePage import BasePage
from selenium.webdriver.common.by import By
import time
from utils.mySettings import pages_url_dir
class Projectmanager(BasePage):

    def to_page(self):
        """
        访问此页面网址
        不必要预先定义页面的打开顺序，因为这样会使整个业务逻辑过于复杂
        考虑到手动测试的时候，是执行到哪一个步骤，需要访问网址，就输入网址并回车访问
        故 我们在每个页面类定义一个访问当前页面的函数
        需要用到的时候就调用
        这个逻辑比写在初始化方法里面更简洁，更易实现和维护
        :return:
        """
        #经过实际运行之后，我们发现这里会有运行失败的情况
        #不是代码错误，而是浏览器更不上故要sleep
        time.sleep(3)
        self.driver.get(pages_url_dir["Projectmanager"])

    def project_status_select_box(self):
        """项目状态搜索下拉框"""
        return self.get_element((By.NAME, "status")) #自己定义的元素等待找元素对象方法
    def project_name_input_box(self):
        """项目名称--输入框的元素定位"""
        return self.get_element((By.CSS_SELECTOR, "form>input"))
    def search_button_box(self):
        """搜索按钮"""
        return self.get_element((By.CSS_SELECTOR,"button[class=\"btn btn-primary\"]"))
    def create_project_box(self):
        """新建项目按钮"""
        return self.get_element((By.CSS_SELECTOR,"a[class=\"btn btn-success\"]"))
    def list_of_project_name_box(self):
        """匹配每一个项目名称返回元素列表"""
        return self.get_elements((By.CSS_SELECTOR,"tbody > tr > :nth-child(1) >a"))
    def list_of_ali_name_box(self):
        """匹配每一个项目别名返回元素列表"""
        return self.get_elements((By.CSS_SELECTOR, "tbody > tr > :nth-child(2)"))



class ProjectmanagerAction(Projectmanager):
    pass

PA = ProjectmanagerAction()