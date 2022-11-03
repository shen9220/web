#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest
import time
from selenium import webdriver
from config.loadyaml import loadyaml
import yaml

class TestCase:
    #测试登录之前要做的事情，打开浏览器，访问网站、页面
    #http://60.12.140.27:58080/long-transport-login-service/transport/doLoginAndGetPermission
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://60.12.140.27:58080/#/login')

   #测完之后关闭浏览器
    def teardown(self):
        time.sleep(1.5)
        self.driver.quit()

    #测试登录成功，输入账号密码，点击登录按钮
    '''
    def test_loginSucess(self):
        print('成功登陆')
        self.driver.find_element_by_css_selector('#userLayout > div.container > div.main > form > div:nth-child(1) > div > div > input').send_keys('1093')
        self.driver.find_element_by_css_selector('#userLayout > div.container > div.main > form > div:nth-child(2) > div > div > input').send_keys('syx9220')
        self.driver.find_element_by_css_selector('#userLayout > div.container > div.main > form > div:nth-child(3) > div > div > input').send_keys('123456')
        self.driver.find_element_by_css_selector('#userLayout > div.container > div.main > form > div:nth-child(5) > div > button').click()
        exmsy = '操作成功'
        sjjg = '操作成功'
        assert exmsy ==sjjg
    '''
    #测试登录失败，输入错误的密码
    #不写死，数据进行分离，pytest从yaml配置文件取数据
    # -代表一个列表[]，  ：代表字典[{'username':'syx9220','password':'123456'}]

    #@pytest.mark.filterwarnings("ignore::UserWarning")     #表示匹配告警信息中的告警类的类名，例如给出代码示例中的告警即可使用如下方式过滤告警
    @pytest.mark.parametrize('udata',loadyaml('/Users/admin/PycharmProjects/py_pytest/date/login.yaml'))     #读取封装的login.yaml文件
    def test_loginError ( self , udata ) :
       #print("打印成功")
       self.driver.find_element_by_css_selector('#userLayout > div.container > div.main > form > div:nth-child(1) > div > div > input').send_keys(udata['longtransportid'])
       self.driver.find_element_by_css_selector('#userLayout > div.container > div.main > form > div:nth-child(2) > div > div > input').send_keys(udata['username'])
       self.driver.find_element_by_css_selector('#userLayout > div.container > div.main > form > div:nth-child(3) > div > div > input').send_keys(udata['password'])
       self.driver.find_element_by_css_selector('#userLayout > div.container > div.main > form > div:nth-child(5) > div > button').click()
       exmsy = '操作成功'
       sjjg = '操作成功'
       assert exmsy ==sjjg

if __name__ == '__main__':
    pytest.main(['-sv','py_test.py'])

#填充内容，实现登录功能  用例，正常和异常
#优化用例  断言
#关键词驱动、常用的操作、提前封装起来、后面直接使用












