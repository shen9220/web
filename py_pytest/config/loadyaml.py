#!/usr/bin/python
# -*- coding:utf-8 -*-

#专门取yaml文件的数据
import yaml

   #要知道自己的yaml文件在哪里
   #封装、方便调用
   #打开yaml文件  r可读取

def loadyaml(fileurl):
    stream = open(fileurl, 'r' )
    #读取文件数据
    date = yaml.load(stream,yaml.FullLoader)
    return date
