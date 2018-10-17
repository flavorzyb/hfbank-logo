# -*- coding: utf-8 -*-
import os
from hfbank_logo.common.file import md5_file, get_all_file_path


image_dir_path = os.path.abspath(os.path.dirname(__file__) + '/../images/baidu')

all_file_list = get_all_file_path(image_dir_path)

hash_map = dict()
for f in all_file_list:
    md5_str = md5_file(f)
    if md5_str in hash_map:
        os.remove(f)
        print f + " has been deleted"
    else:
        hash_map[md5_str] = f
