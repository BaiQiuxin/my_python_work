alien_0 = {
    'color': 'green',
    'points': 5,
}

alien_1 = {
    'color': 'yellow',
    'points': 10,
}

alien_2 = {
    'color': 'red',
    'points': 15,
}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#更现实的情况是，外星人不止三个，而且每个都是由代码自动生成的
#创建一个用于存储外星人的空列表
aliens = []

#创建三十个绿色的外星人
for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        }
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien
        alien['points'] = 10

#显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

#显示创建了多少个外星人
print(f"Total number of aliens: {len(aliens)}")