numofassign = int(input('Enter number of grades to process: '))
studentName = input('Enter student name: ')

total_sum = 0
for n in range(numofassign):
 numbers = float(input('Enter assignment grade: '))
 total_sum += numbers
studentAverage = total_sum / numofassign
print(studentName,'has an average of:', studentAverage)