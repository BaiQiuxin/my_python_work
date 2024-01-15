#向哲煜 2023.12.27
travel = ['xian', 'tokyo', 'beijing', 'london', 'huhehaote']
#按原始顺序打印
print(travel)
#用sorted()按字母顺序打印此列表
print(sorted(travel))
#再次打印该列表，核实排列顺序未变
print(travel)
#用sorted()按与字母顺序相反的顺序打印此列表
print(sorted(travel,reverse=True))
#再次打印该列表，核实列表顺序未变
print(travel)
#用reverse()修改列表顺序并打印以核实
travel.reverse()
print(travel)
#再次调用reve()并打印以核实列表已复原
travel.reverse()
print(travel)
#用sort()修改列表并打印以核实排列顺序确实变了
travel.sort()
print(travel)
#用sort()修改列表，使其元素按与字母元素相反的顺序排列并打印，以核实列表排列顺序确实变了
travel.sort(reverse=True)
print(travel)