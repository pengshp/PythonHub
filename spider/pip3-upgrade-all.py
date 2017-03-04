#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: ??
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: pip3-upgrade-all.py
@time: 2017/3/1 下午10:28
"""
import pip
from subprocess import call


def upgrade_all():
    print("Upgrading all outdated packages......")
    for dist in pip.get_installed_distributions():
        call("pip install --upgrade " + dist.project_name, shell=True)


if __name__ == '__main__':
    upgrade_all()
    print("Upgrade finished!")
