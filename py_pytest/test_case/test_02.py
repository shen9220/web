#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest

class TestCase:

    def setup_class(self):
        print("所有用列执行之前的事情--链接数据库，打开浏览器网页01")

    def treadown_class(self):
        print("所有用例执行之后的事情--关闭浏览器01")

    def setup(self):
        print("所有用列执行之前的事情--链接数据库，打开浏览器网页")

    def treadown(self):
        print("所有用例执行之后的事情--关闭浏览器")

    @pytest.mark.run(order=1)
    def test_01(self):
        print("第一条用例")
        assert 1==1

    @pytest.mark.funner
    @pytest.mark.run(order=3)
    def test_02(self):
        print("第二条用例")
        assert 1==2

    @pytest.mark.run(order=2)
    def test_03(self):
        print("第三条用例")
        assert 1=="1"

#只执行一个或者多个用例（指定用例）
#if __name__ == '__main__':
#    pytest.main(['-sv','-m','funner','test_02.py'])
if __name__ == '__main__':
    pytest.main ( ['-sv', 'test_02.py'] )

#项目实战

