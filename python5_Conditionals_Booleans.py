#Conditionals and Booleans - If, Else, and Elif Statements

language = 'java'
if language=='python':
    print('Langauge is python')
elif language=='java':
    print('Langauge is java')
else:
    print('not matched')

#and
#or
#not
user='admin'
logedin=True
if user=='admin' and logedin:
   print("admin page")
else:
   print('login please')

logedin=False
if user=='admin' or logedin:
   print("admin page")
else:
   print('login please')
   
logedin=False
if not logedin:
   print("not admin page")
else:
   print('login please')
   
#identity object  (is)
a = [1,2,3,4]
b = [1,2,3,4]
print(a==b)
print(id(a))
print(id(b))
print(a is b)
c=a
print(a is c)

#False values
 # false
 # none
 # zero of any numeric type
 # any empty sequence. ex- '',(),[]
 # any empty mapping. ex- {}
condition = False
if condition:
  print("Evaluate true")
else:
  print('evaluate false')
  
condition = None
if condition:
  print("Evaluate true")
else:
  print('evaluate false')
  
condition = 0
if condition:
  print("Evaluate true")
else:
  print('evaluate false')
  
condition = []
if condition:
  print("Evaluate true")
else:
  print('evaluate false')
  
condition = {}
if condition:
  print("Evaluate true")
else:
  print('evaluate false')