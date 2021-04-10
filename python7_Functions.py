# Functions
def funt_hello():
   print('hello function')
  
funt_hello()
#DRY - dont repeat youself

def funt_hello():
   return'hello function22'
  
print(funt_hello())

def funt_hello(greeting):
   return'{} function22'.format(greeting)
  
print(funt_hello('hi'))

#*arg prints the positional values
# **kwargs prints the keys and values

def student(*arg,**kwarg):
  print(arg)
  print(kwarg)
 
student('math','english',name='happy',age='23')
  
courses=['math','english']
info={'name':'happy','age':'23'} 

student(courses,info)
# unpacked the list
student(*courses,**info)


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]
	
print(days_in_month(2020,2))
