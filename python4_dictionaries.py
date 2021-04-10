#Dictionaries - Working with Key-Value Pairs

student = {'name':'hardev','age':23,'subect':['english','math']}
print(student)
print(student['name'])
print(student['age'])
print(student['subect'])
#print(student['phone'])
print(student.get('phone'))
print(student.get('phone','not found'))
student['phone']='7767-9303869'
student['name']='happy'
print(student)
print(student.get('phone','not found'))

#update by single statement
student.update({'name':'hardev','phone':'6555-464616'})
print(student)

#delete the key and value
del student['age']
print(student)

phone= student.pop('phone')
print(student)
print(phone)

# student = {'name':'hardev','age':23,'subect':['english','math']}
#length of key
print(len(student))

#print keys or values
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
  print(key,value)