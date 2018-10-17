# -*- coding: utf-8 -*-
import os
from hfbank_logo.common.file import md5_file, get_all_file_path


image_dir_path = os.path.abspath(os.path.dirname(__file__) + '/../images/baidu')
source_dir_path = os.path.abspath(os.path.dirname(__file__) + '/data/baidu')

logo_image_file_list = get_all_file_path(image_dir_path)
logo_image_md5_map = dict()

for f in logo_image_file_list:
    logo_image_md5_map[md5_file(f)] = f


source_image_file_list = get_all_file_path(source_dir_path)
for f in source_image_file_list:
    md5_str = md5_file(f)
    if md5_str in logo_image_md5_map:
        os.remove(f)
        print f + " 已删除!"
