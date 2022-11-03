#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest

'''
1.scope：可以理解成fixture的作用域，默认：function，还有class、module、package、session四个【常用】
2.autouse：默认：False，需要用例手动调用该fixture；如果是True，所有作用域内的测试用例都会自动调用该fixture
3.name：默认：装饰器的名称，同一模块的fixture相互调用建议写个不同的name
'''

# fixture 用例的前置条件  function对应的是setup，每条用例都会执行scope的前置条件
# autouse 默认是关闭false的，使用fixture需要开启，   不用每次手动，自动调用方法autouse=True
# fixture 后置条件 yield ，关闭系统
# params .param是固定写法

@pytest.fixture(scope='function', autouse=True, params=['加购手机','加购衣服','加购零食'])
def login(request):
    print('登录系统')
    yield request.param
    print('退出系统')

class TestCaase1:
    def test_03( self,login):
        print('登录成功!',login)

    def test_04( self):
        print('登录失败!')

if __name__ == '__main__':
    pytest.main(['-sv', 'py_test1.py'])