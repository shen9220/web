#!/usr/bin/python
# -*- coding:utf-8 -*-
#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest

#module   一个py文件中有多个类，所有类用例执行之前要做的事情、之后的事情

@pytest.fixture(scope='module', autouse=True)
def login():
    print('登录系统')
    yield
    print('退出系统')

class TestCaase1:
    def test_03( self):
        print('登录成功!')

    def test_04( self):
        print('下单成功!')

class TestCaase2:
    def test_03( self):
        print('请支付!')

    def test_04( self):
        print('支付失败!')

if __name__ == '__main__':
    pytest.main(['-sv', 'py_test3.py'])