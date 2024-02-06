list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 1]

print(list1[0:3])
print(list1[0:4:2])
print(list1[::-1])
print(list2[1])
print(list1[::-2])
print(list1[:2:])

students = ['jumoke', 'izu', 'bolaji', 'sussannah']
for student in students:
	print(student)

ans = ''
for student in students:
	ans += student[:2]
print(ans)

ans1 = ''
for student in students:
	ans1 += student[1:2]
print(ans1)