# 向哲煜 2024.2.4

alien_0 ={'color': 'green', 'points': 5}

#访问字典中的值
alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0 ={'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#添加键值对
alien_0 ={'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#从创建一个空字典开始
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#修改字典中的值
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
#一个更有趣的例子
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position:{alien_0['x_position']}")

#向右移动外星人
#根据当前速度确定将外星人向右移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed']  == 'medium':
    x_increment = 2
else:
    #这个外星人的移动速度为快
    x_increment = 3
#新位置为旧位置加上移动距离
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0[]}")