#安装python3下的pygame：
# 以下两种方法更新pip均失败
# pip install --upgrade pip
# pip3 install --upgrade pip
# 以下方法更新pip成功
# python3 -m pip install --upgrade pip

# https://pypi.org/project/pygame/#history 在pygame的历史版本中找到适合自己系统的安装包
# 但没有适合mac10.9的python3的pygame版本，无法安装

# 安装 python2.7
# https://www.python.org/downloads/release/python-2716/ 下载macOS的安装包，根据提示安装
# 此种方法安装的python2不带pip功能，所有需要手动安装python2.7的pip
# 执行如下两行安装pip:
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python get-pip.py

# 下载pygame安装包，拷贝到/Users/xintong/下，然后执行如下代码
# pip2 install pygame - 1.9.3 - cp27 - cp27m - macosx_10_9_intel.whl

# 测试是否安装成功：
# import pygame

# pygame的文件请见forPython2.7项目
