class person:
    university_name="Codegnan university"
    def __init__(self,name,age,gender,phnno,place):
        self.name=name
        self.age=age
        self.phnno=phnno
        self.gender=gender
        self.place=place
    def display(self):
        print(f"Name:{self.name} \nAge:{self.age} \nGender:{self.gender} \nMobile:{self.phnno} \nPlace:{self.place}")
class student(person):
    std_count=0
    def __init__(self,name,age,gender,phnno,place,std_id,course,dept,dept_id,year):
        super().__init__(name,age,gender,phnno,place)
        self.std_id=std_id
        self.dept=dept
        self.dept_id=dept_id
        self.year=year
        self.course=course
        student.std_count+=1
    def display(self):
        print("Student Details:")
        super().display()
        print(f"Student ID:{self.std_id} \nCourse:{self.course} \nDepartment:{self.dept} \ndepartment id:{self.dept_id} \nyear:{self.year}\n")
class faculty(person):
    faculty_count = 0
    def __init__(self,name,age,gender,phnno,place,fac_id,subj,dept,dept_id,exp,edu_bg):
        super().__init__(name,age,gender,phnno,place)
        self.dept=dept
        self.dept_id=dept_id
        self.edu_bg=edu_bg
        self.fac_id=fac_id
        self.exp=exp
        self.subj=subj
        faculty.faculty_count += 1
    def display(self):
        print("Faculty Details")
        super().display()
        print(f"Faculty ID:{self.fac_id} \nSubject:{self.subj} \nDepartment:{self.dept} \ndepartment id:{self.dept_id} \nExperience:{self.exp} \nEducation background:{self.edu_bg}\n")
    

class non_tech(person):
    non_tech = 0
    def __init__(self,name,age,gender,phnno,place,role,dept,dept_id,exp,edu_bg):
        super().__init__(name,age,gender,phnno,place)
        self.role=role
        self.dept=dept
        self.dept_id=dept_id
        self.exp=exp
        self.edu_bg=edu_bg
        non_tech.non_tech += 1
    def display(self):
        print("Non-Technical Staff Details")
        super().display()
        print(f"Role:{self.role} \nDepartment:{self.dept} \ndepartment id:{self.dept_id} \nExperience:{self.exp} \nEducation background:{self.edu_bg}\n")

class security(person):
    security_count = 0
    def __init__(self,name,age,gender,phnno,place,role,block):
        super().__init__(name,age,gender,phnno,place)
        self.role=role
        self.block=block
        security.security_count += 1
    def display(self):
        print("Security Details")
        super().display()
        print(f"Role:{self.role} \nBlock:{self.block}\n")

class cleaning(person):
    cleaning_count = 0
    def __init__(self,name,age,gender,phnno,place,work):
        super().__init__(name,age,gender,phnno,place)
        self.work=work
        cleaning.cleaning_count += 1
    def display(self):
        print("Cleaning Staff Details")
        super().display()
        print(f"Work:{self.work}\n")

class dispensary(person):
    dispensary_count = 0
    def __init__(self,name,age,gender,phnno,place,role):
        super().__init__(name,age,gender,phnno,place)
        self.role=role
        dispensary.dispensary_count += 1
    def display(self):
        print("Dispensary Details")
        super().display()
        print(f"Role:{self.role}\n")
class driver(person):
    driver_count = 0
    def __init__(self,name,age,gender,phnno,place,bus):
        super().__init__(name,age,gender,phnno,place)
        self.bus=bus
        driver.driver_count += 1
    def display(self):
        print("Drivers Details")
        super().display()
        print(f"Bus:{self.bus}\n")
obj=student("deepu",21,"F",7386048604,"Vizag","22vv1a0545","B.TECH","CSE",5,2023)
obj.display()
obj1=faculty("reshu",40,"F",7416364639,"Vijayanagaram","34","AI","CSE",5,"7 years","Ph.D")
obj1.display()
obj2=non_tech("vardhan",35,"M",65789957997,"anakapalli","Lab Assistant","CSE",5,"8 years","B.Tech")
obj2.display()
obj3=security("somu",40,"F",7896560893,"Vizag","Hostel Warden","A")
obj3.display()
obj4=cleaning("joshna",45,"F",9876543210,"srikakulam","Sweeping")
obj4.display()
obj5=driver("hyma",35,"F",9087678905,"palakonda","Driver")
obj5.display()
obj6 = dispensary("siri",35,"F",7542134567,"vizag","wardboy")
obj6.display()
print("count")
print(f"no.of students:{student.std_count}\n no.of faculty:{faculty.faculty_count}\n no.of non_tech:{non_tech.non_tech}\n no.of security:{security.security_count}\n no.of cleaning:{cleaning.cleaning_count}\n no.of dispensary:{dispensary.dispensary_count}\n no.of drivers:{driver.driver_count}\n") 

