class employee: #parent class
    cnt = 0   #initialized to count total employees
    cnt1 = 0 #initialized to find total fulltime employees
    t_sal = 0 #initialized to find total salary of employees
    a_sal = 0 #initialized to find average salary of employees
    def __init__(self,n,f,s,d): #__init___() is constructor to create or initialize employee members
        self.name = n
        self.family = f
        self.salary = s
        self.department = d
        employee.t_sal += s
        employee.cnt += 1
        print("name: %s family: %s salary: %d department: %s"%(self.name,self.family,self.salary,self.department))
    def avg_sal(self): #funtion or method which returns average salary
        a_sal = employee.t_sal/employee.cnt
        print("average sal: ",a_sal)
class fulltime_employee(employee): #child class(inherited from parent class)
    def __init__(self,n,f,s,d):
        employee.__init__(self,n,f,s,d)
        employee.cnt1 += 1
#creating instances for parent class
a = employee("pradeep","vallam",3000,"EEE")
b = employee("praveen","thota",6000,"ECE")
c = employee("naveen","gaddam",5000,"CSE")
print("no of employees: %d total salary: %d"%(a.cnt,a.t_sal))
a.avg_sal()
#creating instances for child class
x = fulltime_employee("revanth","singh",2500,"IT")
y = fulltime_employee("revan","chopra",4500,"IIT")
z = fulltime_employee("vanth","fangh",3500,"BIT")
print("total employees: %d no of fulltime_employees: %d total salary of  employees: %d"%(x.cnt,x.cnt1,x.t_sal))
x.avg_sal()



