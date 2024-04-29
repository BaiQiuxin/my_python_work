""""""

ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"


# 不要将密文拆分成单个的字母，而是要把它拆分成单独的数字
ciphertext = list(ciphertext.split())

# 初始化变量
COLS = 4
ROWS = 5
key = '-1 2 -3 4' #附属表示按照向上的顺序读取列，而正数则表示按照向下的顺序读取列
translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS

# 将key中的字符串转换为整数列表，并将该整数列表分配给key_int:
key_int = [int(i) for i in key.split()]

# 用列表的列表存储矩阵中的每列数据
for k in key_int:
    if k < 0:
        col_items = ciphertext[start:stop]
    elif k > 0:
        col_items = list((reversed(ciphertext[start:stop])))
    translation_matrix[abs(k)-1] = col_items
    start += ROWS
    stop +=ROWS

print(f"\nciphertext = {ciphertext}")
print(f"\ntranslation matrix =", *translation_matrix, sep="\n")
print(f"\nkey length = {len(key_int)}")

# 循环遍历嵌套列表，弹出列表中最后一个元素，并将弹出的元素添加到新创建的列表中
for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + ' '

print("\n")