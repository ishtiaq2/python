class Employee:
    
    raise_amount = 1.04
    number_of_employees = 0

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        Employee.number_of_employees += 1

    def display(self):
        self.first_name
        self.last_name
        return self.first_name, ', ',  self.last_name
    
    #def __str__(self):
     #   return "First Name: %s, LastName: %s, Pay: %d, Employees: %d" % (self.first_name, self.last_name, self.pay, Employee.number_of_employees)        

    def apply_raise(self):
        raise_amt = int(self.pay * self.raise_amount)
        tax = int(raise_amt * .30)
        self.pay = raise_amt - tax

    ''' rais amount for all instances '''
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    ''' creates instance of the class Employee, like a constructor '''
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

emp_str = ['ishtiaq-hussain-30000', 'muqadas-hussain-50000']
first, last, pay = emp_str[0].split('-')
emp_1 = Employee(first, last, int(pay))
first, last, pay = emp_str[1].split('-')
emp_2 = Employee(first, last, int(pay))
emp_3 = emp_1

print'\033[1;32;40m##########################################################################'
print'################################### Comparing instances ##################'
print'##########################################################################\n\033[1;37;40m'
print emp_1
print emp_2
print 'isinstance(emp_1, Employee): ', isinstance(emp_1, Employee)
print 'emp_2 is emp_1: ', emp_2 is emp_1
print 'type(emp_1) == type(emp_2): ', type(emp_1) == type(emp_2)
print 'emp3 is emp1: ', emp_3 is emp_1
print 'emp_1.display(): ', emp_1.display()
print 'emp_1: ', emp_1
print 'emp_2: ', emp_2
print 'emp_3: ', emp_3

print'\n\033[1;32;40m##########################################################################'
print'##################### display instances and class attributes #############'
print'##########################################################################\n\033[1;37;40m'
print 'emp_1.__dict__:'
print emp_1.__dict__
print 'emp_2.__dict__: '
print emp_2.__dict__
print 'Employee.__dict__:'
print Employee.__dict__

print'\n\033[1;32;40m##########################################################################'
print'#########################Raise rais_amoutn by 4% ##########################'
print'##########################################################################\n\033[1;37;40m'

print '\nRaise Amount by 4%:'
emp_1.apply_raise()
print 'empa_1 record after raise: ', emp_1
emp_2.apply_raise()
print 'empa_2 record after raise: ', emp_2

print'\n\033[1;32;40m####################################################################################'
print '###### Changing raise amount using class raise_amount ###############################'
print'#####################################################################################\n\033[1;37;40m'
print 'Changing Class Raise Amount:'
Employee.raise_amount = 1.1218
print 'Raise Amount after changing to 5%:'
emp_1.apply_raise()
print 'empa_1 record after raise: ', emp_1
emp_2.apply_raise()
print 'empa_2 record after raise: ', emp_2
print'\n\033[1;32;40m#######################################################################################'
print '##### Changing raise amount using class raise_amount ###################################'
print'########################################################################################\n'

print'\033[1;32;40m##########################################################################################'
print '############ Changing raise amount using classmethod ###################################'
print'########################################################################################\n\033[1;37;40m'
print 'Changing Class Raise Amount using classmethod:'
Employee.set_raise_amount(1.1218)
print 'Raise Amount after changing to 5%:'
emp_1.apply_raise()
print 'empa_1 record after raise: ', emp_1
emp_2.apply_raise()
print 'empa_2 record after raise: ', emp_2
print'\n\033[1;32;40m##########################################################################################'
print '################################ Changing raise amount using classmethod ###################'
print'#############################################################################################'

print'\n\033[1;32;40m########################################################################'
print '####### Creates instaces of Employee using classmethod from_str(cls, emp_str) ##############'
print'########################################################################\033[1;37;40m'
emp_str_list = ['Rayan-Hussain-50000', 'Yousaf-Hussain-60000']
emp_rayan = Employee.from_string(emp_str_list[0])
emp_yousaf = Employee.from_string(emp_str_list[1])
print 'emp_rayan: ', emp_rayan
print 'emp_yousaf: ', emp_yousaf
print 'emp_rayan.last_name: ', emp_rayan.last_name
print 'emp_yousaf.first_name: ', emp_yousaf.first_name
print'\n########################################################################'

print'\033[1;32;40m##########################################################################'
print'################################### Comparing instances again ##################'
print'##########################################################################\033[1;37;40m\n'
print emp_1
print emp_2
print 'isinstance(emp_1, Employee): ', isinstance(emp_1, Employee)
print 'emp_2 is emp_1: ', emp_2 is emp_1
print 'type(emp_1) == type(emp_2): ', type(emp_1) == type(emp_2)
print 'emp3 is emp1: ', emp_3 is emp_1
print 'emp_1.display(): ', emp_1.display()
print 'emp_1: ', emp_1
print 'emp_2: ', emp_2
print 'emp_3: ', emp_3


print'\n"\033[1;32;40m########################################################################'
print '####### Comparing instaces of Employee created by using classmethod from_str(cls, emp_str) again ##############'
print'########################################################################"\033[1;37;40m'
print 'emp_rayan: ', emp_rayan
print 'emp_yousaf: ', emp_yousaf
print 'emp_rayan.last_name: ', emp_rayan.last_name
print 'emp_yousaf.first_name: ', emp_yousaf.first_name
print'\n\033[1;32;40m########################################################################'


print'\n\n\n"\033[1;32;40m########################################################################'
print '####### Inheritance ##############'
print'########################################################################"\033[1;37;40m'

class Developer(Employee, object):
    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __str__(self):
        return "From Developer:\nFirst Name: %s, LastName: %s, Pay: %d," \
        "Employees: %d" % (self.first_name, self.last_name, self.pay, Employee.number_of_employees)        

dev_1 = Developer('Abbas', 'Khan', 50000, "C++")
print dev_1
print "Developer First Name: {}".format(dev_1.first_name)
print "Developer Last Name: {}".format(dev_1.last_name)

print'\n\n\n"\033[1;32;40m############### class Manager extends Employee #####################################'
class Manager(Employee, object):
    def __init__(self, first, last, pay, employees=None):
        super(Manager, self).__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print emp.first_name

    

dev_2 = Developer('Ali', 'Raza', 5000, "Python")
mgr_1 = Manager('Ayaz', 'Khan', 90000, [dev_1, dev_2])
mgr_1.print_emps()

print'\n\n\n"\033[1;32;40m################# \033[1;37;40mAdding new Employee \033[1;32;40m#############################'
dev_3 = Developer('Waqas', 'Khan', 500000, "Java")
mgr_1.add_emp(dev_3)
mgr_1.print_emps()
print'\n\n\n"\033[1;32;40m################# \033[1;37;40mRemoving one Employee \033[1;32;40m#############################'
mgr_1.remove_emp(dev_2)
mgr_1.print_emps()
print'\n"\033[1;32;40m########################################################################'
print '####### Inheritance ##############'
print'########################################################################"\033[1;37;40m'


print'\n\n\n\033[1;32;40m########################################################################'
print '#################### \033[1;37;40m comparing subclass Inheritance \033[1;32;40m##############'
print'########################################################################"\033[1;37;40m'

print 'isinstance(mgr_1, Employee): ', isinstance(mgr_1, Employee)
print 'isinstance(mgr_1, Developer): ', isinstance(mgr_1, Developer)

print 'issubclass(Manager, Employee): ', issubclass(Manager, Employee)
print 'issubclass(Manager, Developer): ', issubclass(Manager, Developer)

print'\033[1;32;40m########################################################################'
print '#################### \033[1;37;40m comparing subclass Inheritances ends \033[1;32;40m##############'
print'########################################################################"\033[1;37;40m'