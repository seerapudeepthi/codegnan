class person:
    university_name="Codegnan university"
    def __init__(self,name,age,gender,dept,dept_id,edu_bg,phnno):
        self.name=name
        self.age=age
        self.dept=dept
        self.dept_id=dept_id
        self.phnno=phnno
        self.gender=gender
        self.edu_bg=edu_bg
        
    def display(self):
        pass
class student(person):
    std_count=0
    def __init__(self,name,age,std_id,gender,course,edu_bg,dept,dept_id,phnno,year):
        super().__init__(name,age,gender,dept,dept_id,edu_bg,phnno)
        self.std_id=std_id
        self.year=year
        self.course=course
        student.std_count+=1
    def display(self):
        print(f"Name:{self.name} \nAge:{self.age} \nStudent ID:{self.std_id} \nGender:{self.gender} \nDepartment:{self.dept} \ndepartment id:{self.dept_id} \nyear:{self.year} \neducation background:{self.edu_bg}\nmobile no:{self.phnno}")

class faculty(person):
    def __init__(self,name,age,fac_id,dept,dept_id,gender,exp,edu_bg,phnno,subj):
        super().__init__(name,age,gender,dept,dept_id,edu_bg,phnno)
        self.fac_id=fac_id
        self.exp=exp
        self.subj=subj
    def display(self):
        print(f"Name:{self.name} \nAge:{self.age} \nFaculty ID:{self.fac_id} \nGender:{self.gender} \nDepartment:{self.dept} \ndepartment id:{self.dept_id} \nExperience:{self.exp} \neducation background:{self.edu_bg}\nmobile no:{self.phnno}")
        
obj=student("deepu",21,102,"F","CSE","DIPLOMA","CSE",1005,9876543210,4)
print("Student Details:")
print()
obj.display()
print()
obj1=faculty("raji",35,202,"CSE",1005,"F",10,"Ph.D",6390786543,"CSE")
print("Faculty Details:")
print()
obj1.display()

    
    
    

























    
