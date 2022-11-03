#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest

#class 一个类中有多个函数，所有函数执行之前要做的前置条件、后置条件（setupclass）
@pytest.fixture(scope='class', autouse=True)
def login():
    print('登录系统')
    yield
    print('退出系统')

class TestCaase1:
    def test_03( self):
        print('登录成功!')

    def test_04( self):
        print('下单成功!')

if __name__ == '__main__':
    pytest.main(['-sv', 'py_test2.py'])