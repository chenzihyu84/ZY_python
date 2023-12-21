import random
import csv
import pyinputplus as pyip

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

def savetoCSV(fileName:str,data:list[list],subject_nums:int) -> bool:
    fileName += ".csv"
    subjects = [f'科目{i+1}'for i in range(subject_nums)]
    fields = ['姓名']
    fields.extend(subjects)
    with open(fileName,mode='w',encoding='utf-8',newline='') as file:
        try:
            writer = csv.writer(file)
            #fields = None
            writer.writerow(fields)
            writer.writerows(data)
        except:
            return False
        else:
            return True
#students:list[list] = getStudents()
#print(students)

if __name__ == '__main__':

    student_num:int = pyip.inputInt("請輸入學生人數(1~50):",min=1,max=50)
    scores_nums:int = pyip.inputInt("請輸入科目數(1~7):",min=1,max=7)
    students:list[list] = getStudents(student_num,scores_nums)
    fileName = pyip.inputFilename("請輸入檔案名稱:")
    if savetoCSV(fileName=fileName,data=students,subject_nums=scores_nums):
        print("存檔成功")
    else:
        print("存檔失敗")