# -*- coding: utf-8 -*-
import os
import sys
import re
import time
import docx
from docx.shared import RGBColor
from docx.shared import Pt

# 抓取word文件中的图片
def fetch_image(doc_path, desc_path):
    doc = docx.Document(doc_path)
    dict_rel = doc.part._rels  # rels其实是个目录
    for rel in dict_rel:
        rel = dict_rel[rel]
        print("rel", rel.target_ref)
        if "image" in rel.target_ref:
            # create_dir(desc_path)
            img_name = re.findall("/(.*)", rel.target_ref)[0]  # windos:/
            print("img_name", img_name)
            word_name = os.path.splitext(doc_path)[0]
            print("word_name", word_name)
            if os.sep in word_name:
                new_name = word_name.split('\\')[-1]
            else:
                new_name = word_name.split('/')[-1]
            img_name = f'{new_name}_{img_name}'
            with open(f'{desc_path}/{img_name}', "wb") as f:
                f.write(rel.target_part.blob)


def get_image(doc_name,target_folder):
    fetch_image(doc_name, target_folder)


# 创建目录
def create_dir(desc_path):
    if not os.path.exists(desc_path):
        os.makedirs(desc_path)


if __name__ == '__main__':

    get_image(doc_name="docs/test.docx",target_folder='docs/imgs')
