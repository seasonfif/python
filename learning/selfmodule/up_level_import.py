#!/usr/bin/env python
# coding=utf-8
import print_func
import sys
from os import path

# 获取当前文件的父目录
here = path.dirname(__file__)
# 将父目录的父目录加入path路径
sys.path.append(path.dirname(here))

# 导入上级目录中的模块
import del_func
# 导入上级目录另一子目录中的模块
# import anothermodule.add_func as af
from anothermodule.add_func import add_func
print_func.print_func(sys.path,"s","d")

print_func.print_func(add_func(1,3))
print_func.print_func(del_func.del_func(1,3))