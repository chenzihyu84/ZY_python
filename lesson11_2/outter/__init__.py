import random
def getStudents(student_num:int=1,scores_nums:int=2) -> list[list]:
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