# import Modules and Exploring The Standard Library

# import sys
# sys.path.append('path of the my_module if it is in different directory')
# import  my_module
# import my_module as mm
from my_module import *
import random

courses = ['History', 'Math', 'Physics', 'CompSci']
random_courses=random.choice(courses)

print(random_courses)
print(test)
# print(my_module.find_index(courses,'Math'))
# print(mm.find_index(courses,'Math'))
print(find_index(courses,'Math'))
# print(sys.path)