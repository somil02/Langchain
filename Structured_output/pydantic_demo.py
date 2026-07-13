from pydantic import BaseModel, Field
from typing import Optional

class Student (BaseModel):
    name : str
    # default
    age :int = 20
    #optional
    gender: Optional[str] = None # by default it show none
    # field- function -> default values, constraint, description, regex
    cgpa: Optional[float] =Field(default = 0.0,gt=0, lt =10, description = "cgpa should be between 0 to 10" ) 

student = Student(name= 'john', cgpa = 8.2)

print(student.name)
print(student.age)
print(student.gender)
print(student.cgpa)