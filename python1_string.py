print('ghvjhgh')

messsage = 'hello world'
print(messsage)

m="hellos'd world"
print(m)

a="""my name is hardev 
singh sandhu"""
print(a)

#word at speciffied loocation
print(messsage[0])
print(messsage[2:7])
print(messsage[:6])

#length of string
print(len(a))
print(a.upper())
print(a.lower())

#count number off occurrance of letter or word
print(a.count('my'))
print(a.count('s'))

#finf location of the sppecific character or word
print(messsage.find('world'))
print(m.find('world'))
print(m.find('is'))

#replace of previous string
#it return a string after replacing
messsage.replace('world','universe')
print(messsage)

messsage = messsage.replace('world','universe')
print(messsage)

#concatination of string
gretting = 'hello'
name = 'hardev'
new_message= gretting + ' ' + name +' welcome'
print(new_message)
#alternative 
new_message= '{} {} welcome'.format(gretting,name)
print(new_message)
#alternative f string for concatination
new_message= f'{gretting} {name.upper()} welcome'
print(new_message)

#know the methods we use for a variable or string
print(dir(new_message))
print(help(str))
print(help(str.lower))