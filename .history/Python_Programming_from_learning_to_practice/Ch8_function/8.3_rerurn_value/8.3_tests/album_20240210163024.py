# 向哲煜 2024.2.10

def make_album (singer_name, album_name, song_number=None):
    """接受歌手和专辑名，并返回一个包含这两项信息的字典"""
    singer_album = {
        'singer': singer_name,
        'album': album_name,
    }
    
    if song_number:
        singer_album['song number'] = song_number
    
    return singer_album

album_one = make_album('Eric' , 'One')
print(album_one)

album_two = make_album('Mike' , 'Two')
print(album_two)

album_three = make_album('' , '', 5)
print(album_three)