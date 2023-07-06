# age = 30

# name   = 'James'
# {'11' , 
#    '22' , 
#    '44'
#    }

# print(age)
# print(name)

# print(f'Hello sir! My name is {name}. I am {age} years old')

# abc_String = f'Hello sir! My name is {name}. I am {age} years old'


# print(abc_String)

# if name == "James": 
#     print("1")
# elif name == "abc":
#     print("2")
# else :
#     print("A")


# year = 2005

# if year <= 2006 and year >= 2009 :
#     print(f"Wl to {year}")
# else :
#     print(f'Wl to {year}')


# def hello():
#     print("ABC")

# hello()

# def hello(name = "Wolf" , age = 20) : 
#     return "Hello. My name is {}.I'm {} years old.".format(name , age)

# someBody = hello()

# print(someBody)

# def hello(name , age): 
#     print(name , age)

# hello("Jamse")

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)



# fruit_list = ['Orange' , 'Banana' , 'Lemon']

# for x in fruit_list :
#     if x == "Banana" :
#        number = 0;
#        number = number + 1
#        print(f'Yes {number}')
#        break

# arr = [1,2,3,4,5,6,7,8,9]

# for number in arr :
#     if number % 2 == 0 :
#         print(number)
#     else:
#         continue

# numberest = 0;
# for x in arr :
#     if x > numberest :
#         numberest = x
#     else :
#         continue

# print(numberest)

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)


# dog = {"Sala" : 1 , "Mikey" : 2 , "Hinter" : 3}

# print(dog)
# print(dog["Sala"])
# dog["Spider"] = 6
# print(dog)
# del(dog["Hinter"])
# print(dog)


# class Human :

#     def __init__(self , name , age , heigh , gender):
#         self.name = name
#         self.age = age
#         self.heigh = heigh
#         self.gender = gender

#     def show(self):
#         print(f'My name is {self.name}. I am {self.age} years old.')

# obj_Human = Human("James" , 20 , 170 , "Male")
# # obj_Human.show()


# class Animal: 
#     def __init__(self , name):
#         self.name = name

#     def setAge(self , age):
#         self.age = age
#     def getAge(self):
#         return self.age
    
# obj_Animal = Animal("Husky")
# obj_Animal.setAge(5)
# print(obj_Animal.getAge())

# class Addition:
#     answer = 0
#     def __init__(self , f , s):
#         self.f = f
#         self.s = s

#     def display(self):
#         print(f'First number : {self.f}')
#         print(f'Second number : {self.s}')
#         print("Addition of two number = " + str(self.answer))

#     def caculate(self):
#         self.answer = self.f + self.s

# obj_Addition = Addition(10 , 20)
# obj_Addition.caculate()
# obj_Addition.display()

# class Employee:
#     def __init__(self) -> None:
#         print("Employee created...")

#     def __del__(self):
#         print("Desctructor employee...")

# def create_Em():
#     print("Making Obj...")
#     obj = Employee()
#     print("function end...")
#     return obj
    
# print("Calling create_Em() function...")
# obj_Em = create_Em()
# print("Program end...")


# class Person:
#     def __init__(self , name , age , gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def showInfo(self):
#         print(f'Name : {self.name} , age : {self.age} , gender : {self.gender}')
        
# class Student(Person):
#     pass

# x = Student("James" , 20 , True)
# x.showInfo()








