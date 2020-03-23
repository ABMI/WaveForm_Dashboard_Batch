
'''N = int(input())
hw_list = []
for i in range(N):
    hw_list.append(list(map(int, input().split())))

print(hw_list)
print(sorted(hw_list))


6
55 185 2
58 183 3
59 184 2
88 186 1
60 175 2
46 155 6'''


num_student = int(input())
student_list = []

for _ in range(num_student):
    weight, height = map(int, input().split())
    student_list.append((weight, height))

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")