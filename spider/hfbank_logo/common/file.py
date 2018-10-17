# -*- coding: utf-8 -*-
import hashlib
import os


def md5_file(filename):
    rb_file = open(filename, "rb")
    m = hashlib.md5()
    is_eof = False
    while not is_eof:
        content = rb_file.read(4096)
        if content.__len__() == 0:
            is_eof = True
        m.update(content)
    rb_file.close()

    return m.hexdigest()


def get_all_file_path(path):
    result = []

    if os.path.isdir(path):
        file_list = os.listdir(path)
        for f in file_list:
            file_path = os.path.abspath(path + '/' + f)
            children = get_all_file_path(file_path)
            for child in children:
                result.append(child)

    elif os.path.isfile(path):
        result.append(path)

    return result
