# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:42:55 2021

@author: Abdurahman
"""
#Task 1
def prime_number(num1, num2):
    for num in range(num1,num2):
         my_num=num-1
         while my_num>=2:
             if num%my_num==0:
                   break
             elif my_num==2:
                 print(num)
             my_num=my_num-1
        

prime_number(50,100)


#Task 2
def student_info(name,GPA=0):
    print("Student name: "+str(name) +", student GPA is "+str(GPA))
    
student_info("Ahmad",4)
student_info("Mohammed")

#Task 3
def min_and_max():
    student_grades= { 'Physics': 90,
                     'Math': 100, 
                     'history': 70 }
    max_key = max(student_grades, key=student_grades.get)
    min_key = min(student_grades, key=student_grades.get)
    print("Max grade is : "+ str(max_key))
    print("Min grade is : "+ str(min_key))
min_and_max()