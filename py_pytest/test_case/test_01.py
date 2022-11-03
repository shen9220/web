#!/usr/bin/python
# -*- coding:utf-8 -*-
#文件名必须以test_开头或者_test结尾
#类必须以Test开头，不能用init方法
#函数必须以test_开头
#断言使用assert
#打着双引号的内容表示为字符串，如"2"

import pytest

#class 是一个类
class TestCase:

    def setup_class(self):
        print("所有用例执行之前的事情--打开浏览器--链接数据库")

    def teradown_class(self):
        print("所有用例执行之后的事情--关闭浏览器")

    #前置条件
    def setup(self):
        print("用例执行之前的事情--打开浏览器")

    def teradown(self):
        print("用例执行之后的事情--关闭浏览器")

    #一个函数代表一个用例 函数以test_开头
    #顺序器：@ppytest.mark.run

    @pytest.mark.run(number=2)
    def test_01(self):
        print("第一条用例(成功）")
    #断言=成功
        assert 1==1

    #@pytest.mark.going   #设置固定运行方法'-m'，'going'
    @pytest.mark.run(number=1)
    #断言=失败
    def test_02(self):
        print("第二条用例（失败）")
        assert 1=="1"

    @pytest.mark.run(number=3)
    # 断言=失败
    def test_02(self) :
        print("第三条用例（失败）")
        assert 1 == 2

        #顺序执行有两种，1：pytest从上到下执行，2：unittest名字执行
        #只想执行某一条货主某几条用例@pytest.mark.a

#运行用例两种方式：1命令运行，2main方法运行
#多文件只想执行一个文件时填写文件名，想要结果详细加'-sv'

if __name__ == '__main__':
    pytest.main(['-sv','-m','going','test_01.py'])
'''
if __name__ == '__main__':
    pytest.main(['-sv','test_01.py'])
'''