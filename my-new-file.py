# print('Hello Python')
# print('Hello Java')
# print('Hello PHP')

# rahim = 10
# rahim = 20
# print(rahim)

# '' "" """""" ''''''

# a = int(input('Enter A Number:'))
# b = input('Enter A Number:')

# print(type(a))
# print(a + int(b))


# a = 'Bangladesh'
# b = 10

# print(a + str(b))

# a = input('Employee Name:')

# print(a)


# a = int(input('Enter A Number:'))
# b = input('Entar A Number')

# # print(str(a) + b)
# print(a + int(b))

# '' "" ''' ''' """ """

# I Love 'Bangladesh'
# I Love "Bangladesh"

# a = "I Love 'Bangladesh'"
# a = 'I Love "Bangladesh"'
# a = 'I Love Bangladesh'

'''Ami Ai String Ta likheci 
Python Shekhar Jonno'''

# print(type(a))
# print(a.split()[-1])

# print(len(a))

# print(a[: :-1])

# a = 'asd   I love Bangladesh   '

# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.title())

# print(a.index('B'))
# print(a.find('B'))

# print(a.replace('Bangladesh','India'))

# print(a.count('e'))
# print(a.swapcase())
# print(a.strip())
# print(a.split())

# b = input('Enter Your Country Name:')

# b = True

# a = f'I Love {b}'
# print(a)

# print(a.format(b))

# a = 'Bangldesh'
# b = 'INDIA'

# print(a +" " + b)


# a = 'i love \bbangl\tdesh'
# a = 'i \nlove bangladesh'

# print(a)


# a = 'I Love Bang ladesh'
# print(len(a))
# b = a.replace(" ", "")

# print(b)

# print(len(a.replace(" ", "")))

# a = 10

# b = 20

# print(a + b)

# + - * / % ** //

# a = 5
# b = 3

# print(a // b)

# =

# a = 9

# a = a + 10
# print(a)
# a //= 2
# print(a)

# == !=  > <  >= <=

# a = 10
# b = 20

# print(a >= b)

# and or not

# print(not(a < b and a == b))

# is is not

# print(a is not b)

# in not in

# my_var =  'i love bangladesh'

# print("z" not in my_var)

# & | ~ ^ << >> 
#     8 4 2 1
#     -------
# 0 = 0 0 0 0
# 1 = 0 0 0 1
# 2 = 0 0 1 0
# 3 = 0 0 1 1
# 4 = 0 1 0 0
# 5 = 0 1 0 1
# 6 = 0 1 1 0
# 7 = 0 1 1 1
# 8 = 1 0 0 0

# 0 1 0 1
# 0 0 1 1
# -----------
# 0 0 0 1
#  0 1 1 1
# print( ~ 3)


# if else


# a = 'sdf'

# b = 'sd'

# if a == b:
#     print('Hello Bangladesh')
# elif a < b :
#     print('I am Bigger than B')
# elif a < b :
#     print('B is Bigger than A')
# else:
#     print('Ami Jani na')

# a = int(input('Enter Student\'s Result :'))

# if a > 100 or a < 0:
#     print('Invalid Number')
# else:
#     if a >= 80:
#         print("A+")
#     elif a >= 70:
#         print('A')
#     elif a >= 60:
#         print("A-")
#     else:
#         print('Fail')

# if a <= 100 and a >= 0:
#     if a >= 80:
#         print("A+")
#     elif a >= 70:
#         print('A')
#     elif a >= 60:
#         print("A-")
#     else:
#         print('Fail')    
# else:
#    print('Invalid Number')

# a = int(input('Enter A Number :'))

# if a % 2 == 0:
#     print('Its A Even number')
# else:
#     print('Its A Odd Number')

# while
# for

#while #condition :
    #output
# a = 11
# while a <= 20:
#     print('I love Bangladesh')
#     # a = a +1
#     a += 1

# a = True 1
# b  = False 0

# while True:
#     print('I love Bangladesh')

# a = 0

# while a <= 10:
#     print(a)
#     if a == 5:
#         break
#     a += 1

# while a < 10:
#     a += 1
#     if a == 5:
#         continue
#     print(a)

# while a < 10:
#     a += 1
#     if a == 5:
#         continue
#     print(a)


# a = 'I Love Bangladesh'

# # print('z' in a)

# for my_ver in a:
#     # if my_ver == 'e':
#     #     break
#     print(my_ver, end="")

# for my_ver in range(1,11):
#     print(my_ver)

# for i in range(len(a)):
#     print(i , a[i])

# print(a[10])

# print(a[0:10])

# a = 1

# while a <=10:
#     print(a)
#     a+=1

# for i in range(1,11):
#     print(i)

# for i in range(1,6):
#     for j in range(i):
#         print("*", end=" ")
#     print()

    # List /  Tuple /  Dictionary / Set


# a = [12,'bangladesh', True, 12.23,12,12,12,12,12]

# print(a)

# a = 'I Love Bangladesh'

# print(a[2])

# print(len(a))

# for i in range(len(a)):
#     print(i , a[i])

# print(a.index('bangladesh'))

# a.append('India')
# print(a)

# a.insert(2,'USA')
# print(a)

# a.remove(True)
# print(a)

# a.pop()
# print(a)
# b = a.copy()
# b.remove(True)
# print(a)
# print(b)

# a = [ 2,5,1,6,8,23,21,13]
# a.sort()
# a.reverse()
# a.clear()
# print(a)


# country_name_show = []

# while True:
#     country_name_input = input('Enter A Country:').title()
#     if country_name_input == 'exit'.title():
#         break
#     elif country_name_input == 'pop'.title():
#         country_name_show.pop()
#         print(country_name_show)
#     elif country_name_input == 'remove'.title():
#         remove_item = input('Enter A Country:').title()
#         country_name_show.remove(remove_item)
#         print(country_name_show)
#     else:
#         country_name_show.append(country_name_input)
#         print(country_name_show)

# a = (12,'bangladesh', True, 12.23)
# print(a)
# # print(type(a))
# # print(a.count(12))
# # print(a.index(True))
# b = list(a)
# b.remove(12)
# a = tuple(b)
# print(a)
# print(b)


# a = [12,23,24,45]
# print(len(a))

# b = ['asdf','asdf','asdf']

# a.extend(b)

# print(a)
# print(len(a))

# a = [12,'bangladesh', True, 12,12,12,12,12]

# using while Loop

# while 12 in a:
#     a.remove(12)

# print(a)

# # Using For Loop
# x = []
# for i in a:
#     if i != 12:
#         x.append(i)

# print(x)

# print(len(a))
# print(a.count(12))
# b = 0
# for i in a:
#     # a.remove(12)
#     if i == 12:
#         a.remove(12)
#         if a.count(12) <= 0:
#             break
#         b += 1
#         print(b)

# print(a)


# a = {'name':'rahim','age':40}

# print(a['name'])
# print(a.keys())
# print(a.values())
# a.update({'roll':'Executive'})
# print(a)
# print(a.get('name'))

# a.pop('age')
# a.popitem()
# print(a)
# b  = a.copy()
# b.popitem()
# print(a)
# print(b)
# a.clear()
# b = a.items()
# print(b)

# for i, j in a.items():
#     print(f'{i}: {j}')

# a = {'bangladesh','india','pakistahn'}
# b = {'canada','UK','USA','bangladesh'}
# a.update(b)
# c = b.difference(a)

# print(c)

# c = a & b 

# c = a.intersection(b)

# c = a.union(b)

# print(len(a))

# print(type(a))

# print(a)
# for i in a:
#     print(i)

# a.add('Singapure')
# b = a.copy()
# b.add('Singapure')
# print(a)
# print(b)
# a.clear()
# print(a)

# a.discard('pakistahn')
# a.pop()

# print(a)

# def myfunc():
#     print('I love bangladesh')

# myfunc()

# def my_func(*num):
#     print(num)

# my_func('f','k','i')

# a = lambda x : x + 10

# print(a(6))

# a = lambda: 'Hello World'

# print(a())

# x = int(input('Enter A Number : '))

# a = lambda g : "even" if x % 2 == 0 else 'Odd'

# print(a(x))

# a = 30
# b = 20

# if a < b :
#     print('a is smaller than b')
# else:
#     print('a is bigger than b')

# x = 'a is smaller than b' if a < b else 'a is bigger than b'

# print(x)
# print('a is smaller than b') if a < b else print('a is bigger than b')

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n -1)

# # 5 X 4 X 3 X 2 X 1

# print(factorial(5))

# a = [i ** 2 for i in range(5)]

# print(a)

# a = []

# for i in range(5):
#     a.append(i**2)

# print(a)

# x = 1
# while x <= 5:
#     print(x)
#     x+=1

# x = 1

# while x <= 5: print(x); x+=1

# a = 'i love bangladesh'

# print(a[:6])


# a = open('E:\\Universal IT\\Batch - 109\\My_file.txt', "r")
# a = open('E:/Universal IT/Batch - 109/My_file.txt', "r")
# a = open('E:/Universal IT/Batch - 123/New File.txt', "r")

# print(a.read())

# a = open('E:/Universal IT/Batch - 109/My_file.txt', "w")
# a = open('E:/Universal IT/Batch - 109/My_file.txt', "a")

# a.write('This is our New File For File Handaling-2.')

# a = open('E:/Universal IT/Batch - 109/My_file.txt', "r")
# print(a.read())

# import os

# old_name = 'E:/Universal IT/Batch - 109/My_file.txt'
# new_name = 'E:/Universal IT/Batch - 109/test.txt'

# os.rename('test.txt','my_file.txt')

# os.remove('xxxMy_file.txt')
# os.mkdir('My New Folder')
# os.rmdir('My New Folder')

# if os.path.exists('my_file.txt'):
#     os.remove('my_file.txt')
# else:
#     print('file not Exist')

# try:
#     a = open('E:/Universal IT/Batch - 109/My_file.txt', "x")

#     a.write('This is our New File For File Handaling-2.')

#     a = open('E:/Universal IT/Batch - 109/My_file.txt', "r")
#     print(a.read())
# except Exception as e:
#     print(e)
# finally:
#     print('ghghh')


# a = 'i love bangladesh'

# print(a[:6])

# try:
#     pass
# except:
#     pass

# from my_modle import my_fun

# print(asdf)

# print(my_fun())

# import datetime

# a = datetime.datetime.now()
# print(a.strftime('%I : %M : %S %p'))

# import pandas as pd

# data = {
#     'Name' : ['Rahim', 'Karim', 'Abdul'],
#     'Age' : [25,30,35],
#     'City' : ['Dhaka', 'Khulna','Rajshahi']
# }

# df = pd.DataFrame(data)
# # print(df)
# df.to_csv('output.csv', index=False)


# myclass
# MyFirstClass
# my_first_class

# class MyClass:
    # a = 10
    # b = 20

#     def myfun(self):
#         return 'Hello'


# x = MyClass()

# print(x.myfun())

# class A:
#     a = 10
#     b = 20

# class B(A):
#     c = 30
#     d = 40

# x = B()

# print(x.a)

# class MyClass:
#     def __init__(self):
#         print('Hello World, I Am Running.')
    
#     a = 10
#     b = 20
#     c = 'I Love Bangladesh'


# x = MyClass()

# print(x.a)

# class MyClass():
#     def myfun(self,num1,num2):
#         # print(num1 + num2)
#         self.asdf = num1
#         self.zxc = num2


# x = MyClass()

# x.myfun(12,23)


# class Person:
#     def __init__(self,name,age):
#         self.a = name
#         self.b = age
    
    # def my_var(self):
    #     self.a = 'Rahim'
    #     self.b = 30
    #     return self.a , self.b

    # def greetings(self):        
    #     return f"Hello, My Name is {self.a} and I am {self.b} Years Old."
    

# x = Person('Rahim',40)
# x = Person()
# # x.my_var()
# print(x.greetings())

# print(x.my_var())


# class Car:
#     def move(self):
#         print("Drive")
    
# class Plane:
#     def move(self):
#         print("Fly")

# class Boat:
#     def move(self):
#         print("Sail")
        

# car = Car()
# boat = Boat()
# plane = Plane()

# print(car.move())
# print(boat.move())
# print(plane.move())

# for i in (car,boat,plane):
#     i.move()

class FileHandling:
    def __init__(self,filename):
        self.file = open(filename,"w")
        print("Your File opened")
    
    def write_data(self,data):
        self.file.write(data)

    def __del__(self):
        self.file.close()
        print('Writeing Has been Completed.')

x = FileHandling('My_file.txt')
x.write_data('Class Sesh.')