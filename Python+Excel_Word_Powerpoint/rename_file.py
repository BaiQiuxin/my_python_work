"""用Python批量修改文件后缀"""
import os
import shutil

def change_filename(to_change_files, old_ext, new_ext):
    """批量将指定旧后缀修改为指定新后缀"""
    # 依次查找各个文件
    for filename in to_change_files:
        potion = os.path.splitext(filename)
        # 如果找到待更换的旧后缀
        if potion[1] == old_ext:
            # 将后缀改为指定的新后缀
            new_filename = potion[0] + new_ext
            # 重命名文件
            os.rename(filename, new_filename)


def change_to_rar(to_rar_files):
    """将文件后缀修改为.rar"""
    # 依次查找各个文件
    for filename in to_rar_files:
        potion = os.path.splitext(filename)
        # 如果后缀不是.rar
        if potion[1] != '.rar':
            # 将后缀改为.rar
            newname = potion[0] + '.rar'
            # 重命名文件
            os.rename(filename, newname)


def move_files(target_files):
    """将指定后缀的文件移动到指定目录"""
    for filename in target_files:
        potion = os.path.splitext(filename)
        if potion[1] == '.txt':
            shutil.move(filename, 'F:/GAME/MANGA/')

if __name__ == "__main__":
    os.chdir(r'D:\Game\解压')
    # 列出当前目录下的所有文件
    files = os.listdir('.')
    change_to_rar(files)
