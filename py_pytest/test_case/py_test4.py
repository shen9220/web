#!/usr/bin/python
# -*- coding:utf-8 -*-

import pytest

# fixture 用例的前置条件  function对应的是setup，每条用例都会执行scope的前置条件
# autouse 默认是关闭false的，使用fixture需要开启，   不用每次手动，自动调用方法autouse=True
# fixture 后置条件 yield ，关闭系统
# params .param是固定写法

# ids 是给用例取名字(不可中文）

# name是给fixture函数取小名（login是大名，name=小名)
@pytest.fixture(scope='function', autouse=True, params=['手机', '衣服', '零食'], ids=['aa', 'bb', 'cc'], name='A')
def login(request):
    print('登录系统')
    yield request.param
    print('退出系统')

class TestCase1:
    def test_03(self, A):  #name=A，A是小名
        print('登录成功,加购了', A)

    def test_04(self):
        print('下单成功!')

if __name__ == '__main__':
    pytest.main(['-sv', 'py_test3.py'])