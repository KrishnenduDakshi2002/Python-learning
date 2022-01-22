#base class
class person(object):
    
    # contructor
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
        
    def DisplayNameId(self):
        print("Hii ! I am {}, and my id is {}".format(self.name,self.idnumber))
   
   
# child class

class employ(person):
    
    def __init__(self,name,idnumber,salary,post):
        self.name = name     
        self.idnumber = idnumber     
        self.salary = salary    
        self.post = post
        
    def DisplayEmploySalaryPost(self):
        print("I am posted in the department of {} , and my salary is {}".format(self.post,self.salary))     
        
#
class SDE(employ,person):
    def __init__(self,name,idnumber,salary,post,workingProject):
        self.name = name     
        self.idnumber = idnumber     
        self.salary = salary    
        self.post = post
        self.workingProject = workingProject
        
    def workingProj(self):
        print("I am working on the project {}".format(self.workingProject))
    
        
Krishnendu = SDE('Krishnendu',123,120000,"Software developement","Chrome dev")
print("Hi there ! {}".format(Krishnendu.name))
Krishnendu.DisplayNameId()
Krishnendu.DisplayEmploySalaryPost()
Krishnendu.workingProj()
