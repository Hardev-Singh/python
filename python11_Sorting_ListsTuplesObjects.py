# Sorting Lists, Tuples, and Objects
li = [2,5,8,86,4,8,5,8,5]
new_li = sorted(li)
# new_li = sorted(li, reversed=True)
print(new_li)
##or 
li.sort()
# li.sort(reversed=True)
print(li)

tup = (5,5,8,1,8,7,1,8,)
s_tup = sorted(tup)
print('tuple\t',s_tup)

dict = {'name':'hardev','age':23,'lan':'pun'}
s_dict = sorted(dict)
print(s_dict)

#sorting with the absolute value
lis = [-5,-3,5,-7,3,9]
s_lis = sorted(lis, key=abs)
print(s_lis)


class Employee():
  def __init__(self,name,age,salary):
    self.name=name
    self.age=age
    self.salary=salary
	  
  def ___repr__(self):
      return '({},{},${})'.format(self.name,self.age,self.salary)
	  
from operator import attrgetter
e1 = Employee('happy',23,2422)
e2 = Employee('hardev',53,222)
e3 = Employee('golu',63,2429992)

employees = [e1,e2,e3]
print(employees)
# custom function tsort
# def e_sort(emp):
    # return emp.age
	
s_employees = sorted(employees,key=attrgetter('age'))
print(s_employees)

