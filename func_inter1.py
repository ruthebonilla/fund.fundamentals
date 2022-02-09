#1 UPDATE VALUES
x = [ [5,2,3], [10,8,9] ] 

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

#--- Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]
x[1][0] = 15
print(x)

#--- Change last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students[0])

#--- In sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

#--- Change value 20 in z to 30
z[0]['y'] = 30
print(z[0])
# ////////////////////////////////////////////////////////////////////////////////////////////

#2 ITERATE THROUGH A LIST OF DICTIONARIES
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in some_list:
        print(i)

iterateDictionary(students) 
# //////////////////////////////////////////////////////////////////////////////////////////////////

#3 GET VALUES FROM A LIST OF DICTIONARIES
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])
        
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
# ///////////////////////////////////////////////////////////////////////////////////////////////////

# 4 ITERATE THROUGH A DICTIONARY WITH LIST VALUES
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for a, b in some_dict.items():
        print(len(some_dict[a]))
        print(a)
        print(b)

printInfo(dojo)

