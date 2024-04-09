"""以列表的形式加载一个文本文件

参数：
文本文件的名字

异常：
若没有找到文件，则报告IOError类型的异常

返回值;
一个包含文本文件中所有单词小写形式的列表

要求导入的模块 sys

"""

import sys

def load_file(file):
    """打开文本文件，并以列表的形式返回文件内容对应的小写字母"""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [text.lower() for text in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f"{e}\nError opening {file}. Terminating program.", file=sys.stderr)
