# -*- coding:utf8 -*-
__author__ = 'ltyao'
import os
from os.path import join, getsize


def cmp_size(left_dir, right_dir):
    for root, dirs, files in os.walk(left_dir):
        for file_name in files:
            left = getsize(join(root, file_name))
            right = getsize(join(root.replace(left_dir, right_dir), file_name))
            if cmp(left, right) != 0:
                print root, file_name, left - right


