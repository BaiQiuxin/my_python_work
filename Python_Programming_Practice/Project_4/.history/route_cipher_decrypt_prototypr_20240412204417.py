""""""

ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"


# 不要将密文拆分成单个的字母，而是要把它拆分成单独的数字
ciphertext = list(ciphertext.split())

# 初始化变量
COLS = 4