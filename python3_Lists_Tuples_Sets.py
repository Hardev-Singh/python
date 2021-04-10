#Lists, Tuples, and Sets

#list
#empty list
   #empty_list=[]
   #empty_list=list()

courses=['math','physics','english','comp']
print(courses)
print(len(courses))
print(courses[2])
print(courses[1:3])
#-1 always print last index of list
print(courses[-1])

#insert new values
courses.append('art')
print(courses)
#to specific location
courses.insert(0,'hindi')
print(courses)

#to add two list
courses2=['punjabi', 'edu']
courses.extend(courses2)
print(courses)

#to remove value
courses.remove('art')
print(courses)
#to remove last value
popped = courses.pop()
print(popped)
print(courses)

#reverse of list
courses.reverse()
print(courses)

#sorting
courses.sort()
print(courses)

courses.sort(reverse=True)
print(courses)

#sorted function to not alter the original list
sorted_courses=sorted(courses)
print(sorted_courses)

#min max sum of numbered list
num =[1,5,5,8,1,4]
num.sort()
print(num)
print(max(num))
print(min(num))
print(sum(num))

#index of the value
print(courses)
print(courses.index('math'))

#to know the value is present or not
print('math' in courses)

#in also work for for loop
#index also
for index, item in enumerate(courses, start=1):
 print(index,item)
 #for index, iteam in enumerate(courses):
# print(index,iteam)
 
 #to print a list in string
courses_str=' - '.join(courses)
print(courses_str)
# to again convert string to list
newList= courses_str.split(' - ')
print(newList)

#tuples
#empty tuples
   #empty_tuples=()
   #empty_tuples=tuples()
  
#mutable
list1= ['apple','grapes','banana','orange']
list2= list1
print(list1)
print(list2)

list1[0]='berry'
print(list1)
print(list2)
 
 
 
 #change in one list also change value of other list so this solved by tuples
 #immutables
tuple_1=('apple','grapes','banana','orange')
tuple2= tuple_1
print(tuple_1)
print(tuple2)

#in tuples we cannot append, delete and so on. only loop or view
# tuple_1[0]='berry'
# print(tuple_1)
# print(tuple2)


#Sets
#empty sets
  #empty_sets={}  !this is not right. its dict
  #empty_sets=set()

#unordere and no duplicates
sets_1={'apple','grapes','banana','orange','grapes'}
sets_2={'apple','grapes','banana','cherry'}
print(sets_1)
#it optimise the search of value 
print('grapes' in sets_1)
#similar values from set
print(sets_1.intersection(sets_2))
#different values from set
print(sets_1.difference(sets_2))
#all values from set
print(sets_1.union(sets_2))