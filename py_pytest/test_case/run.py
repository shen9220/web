#!/usr/bin/python
# -*- coding:utf-8 -*-
# 测试报告  unittest、pytest+allure插件生产报告
# 需要配置环境
# 1、安装allure-pytest 生成测试数据
# 2、下载 commaandline 压缩包  解压在
# 3、配置一下环境变量


# 生成测试报告：执行用例
import os
import pytest

# alluredir    生成数据，创建文件夹测试数据allure-result
# 生成测试报告
# allure generate 执行测试数据  -o生成测试报告   测试报告的文件夹reports（报告要看index.html）



if __name__ == '__main__':
    pytest.main(['py_test.py','--alluredir','./allure-result'])
    os.system('allure generate ./allure-result -o ./reports')