# 向哲煜 2024.1.16

#删除前缀

nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')
print(nostarch_url.removeprefix('https://'))

simple_url = nostarch_url.removeprefix('https://')
print(simple_url)
