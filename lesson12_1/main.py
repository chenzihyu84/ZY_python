from random import randint,choices
import csv
from csv import DictWriter
import pyinputplus as pyip

def getStudents(nums:int) -> list[dict]:
    
 
    students:list[dict] = []
    with open('names.txt', mode='r',encoding = 'utf-8') as file:
        names:str = file.read()
    namesList:list[str] = names.split('\n')
    names = choices(namesList,k=nums)
    
    for i in range(nums):
        stu = {
        '姓名':names[i],
        '國文':randint(45,100),
        '數學':randint(45,100),
        '英文':randint(45,100),
        '地理':randint(45,100),
        }
        students.append(stu)
    return students

def save_to_csv(students:list[dict],fileName:str)->None:
    fileNameWithExtension:list = fileName + '.csv'
    with open(fileNameWithExtension,mode = 'w',encoding = 'utf-8',newline = '') as file:
        fieldnames:list[str] = ['姓名','國文','數學','英文','地理']
        writer:DictWriter= csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
    print("寫入成功")

if __name__ == "__main__":
    student_num:int = pyip.inputInt("請輸入學生人數(1~50):",min=1,max=50)
    students:list[dict] = getStudents(student_num)
    fileName = pyip.inputFilename("請輸入檔案名稱:")
    save_to_csv(students,fileName)