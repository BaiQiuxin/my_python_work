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
key_int = 