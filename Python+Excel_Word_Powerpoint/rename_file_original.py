"""用Python批量修改文件后缀为rar"""
import os

if __name__ == "__main__":
    os.chdir('D:/Game/解压/')
    # 列出当前目录下的所有文件
    files = os.listdir('./')
    for filename in files:
        potion = os.path.splitext(filename)
        # 如果后缀不是.rar
        if potion[1] != '.rar':
            # 将后缀改为.rar
            newname = potion[0] + '.rar'
            os.rename(filename, newname)
