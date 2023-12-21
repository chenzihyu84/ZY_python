
import pyinputplus as pyip
from outter.tools import savetoCSV
from outter import getStudents


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