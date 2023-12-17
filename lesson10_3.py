import random
import pyinputplus as pyip

def getStudents(student_num:int,scores_nums:int) -> list[list]:
    '''
    參數:student_num -> 學生人數
    參數:scores_nums -> 科目數
    '''
    with open('names.txt', mode='r',encoding = 'utf-8') as file:
        names:str = file.read()

    namesList:list[str] = names.split('\n')
    students:list[list] = []

    names:list[str] = random.choices(namesList,k=student_num)
    for name in names:
        stu:list[int|str] = []
        stu.append(name)
        for i in range(scores_nums):
            stu.append(random.randint(40,100))
        students.append(stu)

    return students

#students:list[list] = getStudents()
#print(students)

if __name__ == '__main__':

    student_num:int = pyip.inputInt("請輸入學生人數(1~50):",min=1,max=50)
    scores_nums:int = pyip.inputInt("請輸入科目數(1~7):",min=1,max=7)
    students:list[list] = getStudents(student_num,scores_nums)
    print(students)
    