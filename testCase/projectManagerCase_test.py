# coding=utf-8
# projectManagerCase
# 2020/12/25

import pytest
from pages.projectManger import PA
class TestprojectManagerCase:
    def test_project_name_search(self):
        """
        模糊查询测试用例：当我通过某字符串搜索项目的时候
        查询出来的每条信息，他的名称或者别名至少有一个包含该字符串
        :return:
        """
        PA.to_page()
        """1 选定文本、输入、搜索"""
        project_name = "南海"
        PA.project_name_input_box().send_keys(project_name)
        PA.search_button_box().click()

        """2 获取项目名称列表，获取项目别名列表"""
        project_name_sli = PA.list_of_project_name_box()
        project_ali_name_sli = PA.list_of_ali_name_box()

        """3 验证断言，搜索出来的列表，别名或项目名称中至少有一个包含搜索文本"""
        for pj_name in project_name_sli:
            as1 = project_name in pj_name.text
            as2 = project_name in project_ali_name_sli[project_name_sli.index(pj_name)].text
            assert as1 or as2

if __name__ == '__main__':
    pytest.main()
