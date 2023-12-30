
import pyinputplus as pyip
from tools import getStudents,save_to_csv,save_to_excel


if __name__ == "__main__":
    student_num:int = pyip.inputInt("請輸入學生人數(1~50):",min=1,max=50)
    students:list[dict] = getStudents(student_num)
    fileName:str = pyip.inputFilename("請輸入檔案名稱:")
    format = pyip.inputChoice(["1","2"],"請問要輸出哪一個格式:\n按1 excel\n按2 csv\n 請選擇:")
    if format == "1":
        save_to_excel(students,fileName)
    else:
    
        save_to_csv(students,fileName)