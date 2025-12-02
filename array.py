from wsgiref.util import request_uri

import array as MyArray

def DisplayContent(arr):
    for x in range(len(arr)):
        print(arr[x], end=" ")
#search
def search(arr,k):
    for x in range(len(arr)):
        if k == arr[x]:
            return True
    else:
        return False

grade = MyArray.array('i',[0]*5)
print("Enter all grades")
for x in range(len(grade)):
    grade[x] = int(input())
#bubble sort
for x in range(len(grade)):
    for y in range(len(grade)-1):
        if (grade[y]>grade[y+1]):
            temp = grade[y]
            grade[y]=grade[y+1]
            grade[y+1] = temp
DisplayContent(grade)

key = int(input("Enter grade: "))
if(search(grade,key)):
    print('found')
else:
    print('not found')

