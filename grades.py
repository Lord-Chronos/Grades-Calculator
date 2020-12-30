y2_grades = []
y3_grades = []
unknown_2 = 0
unknown_3 = 0
true_y3 = 0

print("Input Module Percentages for 2nd Year")
print("('?' for unkown grade)")
for i in range(8):
    grade = input("M-" + str(i+1) + ": ")
    if grade == '?':
        unknown_2 += 1
    else:
        y2_grades.append(int(grade))

print("Now 3rd Year Modules: ")

for i in range(8):
    grade = input("M-" + str(i+1) + ": ")
    if grade == '?':
        unknown_3 += 1
    else:
        y3_grades.append(int(grade))

y2_grades.sort(reverse=True)
y3_grades.sort(reverse=True)


if len(y2_grades) != 0:
    y2_average = sum(y2_grades)/ len(y2_grades)
else:
    y2_average = 50

if len(y3_grades) != 0:
    y3_average = sum(y3_grades) / len(y3_grades)
else:
    y3_average = 50


def Average_Calc(y2_grads, y3_grads, average_2, average_3, unknown_2, unknown_3):
    y2_grad = y2_grads.copy()
    y3_grad = y3_grads.copy()

    for i in range(unknown_2):
        y2_grad.append(average_2)

    for i in range(unknown_3):
        y3_grad.append(average_3)


    true_y3_3w = 0
    true_y3_2w = 0


    for i in range(4):
        true_y3_3w += (y3_grad[i])

    for i in range(4):
        true_y3_2w += (y3_grad[i+4] )

    avg_true_y3_3w = true_y3_3w/4
    avg_true_y3_2W = true_y3_2w/4

    return round((((avg_true_y3_2W*2) + (avg_true_y3_3w*3) +(sum(y2_grad)/8))/6),2)

print("\n")

print("-------------------------------------------")

print("\nFINAL GRADE")


print("\nBased on Averages")
print(str(Average_Calc(y2_grades, y3_grades,y2_average,y3_average,unknown_2,unknown_3)) + "%")

print("\nWorst Case")
print(str(Average_Calc(y2_grades, y3_grades,0,0,unknown_2,unknown_3)) + "%")

print("\nBest Case")
print(str(Average_Calc(y2_grades, y3_grades,70,70,unknown_2,unknown_3)) + "%")

