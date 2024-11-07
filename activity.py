print('please enter the grade of students (it should be only between 40-100)')

grade = []
studentnumber = 1
systemloop = True
totalgrade = 0
passedstudentnumber = 0

while systemloop == True:
    studentgrade = input(f'student #{studentnumber}: ')
    if studentgrade.isdigit():
        studentgrade = int(studentgrade)
        if studentgrade >= 40 and studentgrade <= 100:
            grade.append(studentgrade)
            studentnumber += 1
            continue
        else:
            print('[invalid input] enter a number between 40 and 100.')
            continue
    elif studentgrade.lower() == 'done':
        systemloop = False
    else:
        print('[invalid input] Enter a number.')
        continue
else:
    if grade != []:
        for gradeX in grade:
            totalgrade += gradeX
            average = totalgrade / len(grade)
        else:
            print(f'average grade: {average:.2f}')
        for gradeX in grade:
            if gradeX >= 75:
                passedstudentnumber += 1
        else:
            print(f'the number of passed students: {passedstudentnumber}')
            passpercentage = (passedstudentnumber / len(grade)) * 100
            print(f'pass percentage: {passpercentage:.2f}%')
    else:
        print('no grade have been entered.')