num1 = 42  #variable declaration, initialize number
num2 = 2.3  #variable declaration, initialize number
boolean = True #initalizing boolean as true.
string = 'Hello World'  #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, setting list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #declaring person and setting it to an object.
fruit = ('blueberry', 'strawberry', 'banana') #declaring a key, setting it's potential arguements
print(type(fruit)) #log statement, type check, access value
print(pizza_toppings[1]) #log statement, access value, access index
pizza_toppings.append('Mushrooms') #access pizza toppings, add mushrooms to list
print(person['name']) #log statement, access value name
person['name'] = 'George' #access value name of person. set to george
person['eye_color'] = 'blue' #access person, access eye color and change to blue
print(fruit[2]) #log statement , print index 2 of fruit

if num1 > 45:   #if statemet
    print("It's greater")  #log statement
else:           #else stament
    print("It's lower") #log statement

if len(string) < 5:  #if statemet
    print("It's a short word!") #log statement
elif len(string) > 15:
    print("It's a long word!") #log statement
else:
    print("Just right!")#log statement

for x in range(5):  # for loop
    print(x)  #log statement
for x in range(2,5):  # for loop
    print(x)  #log statement
for x in range(2,10,3):  # for loop
    print(x)  #log statement
x = 0
while(x < 5):   #while loop
    print(x)  #log statement
    x += 1   #increment x by 1

pizza_toppings.pop()  #remove the last value from pizza toppings
pizza_toppings.pop(1) #remove the value of pizza toppings at index 1

print(person)  #log statement
person.pop('eye_color') #remove this value from person
print(person)  #log statement 

for topping in pizza_toppings:  #initilaizing for loop
    if topping == 'Pepperoni':   #if statement
        continue        #if true, continue to next line
    print('After 1st if statement')  #log statement
    if topping == 'Olives': #if statement
        break  # if true, break the loop

def print_hello_ten_times(): #delcaring function
    for num in range(10): #setting the for loop to iterate through the range 0-10
        print('Hello')  #log statement

print_hello_ten_times()  #this will print hello 10 times

def print_hello_x_times(x): #declaring a fuction
    for num in range(x): #setting the function
        print('Hello')  #log statement

print_hello_x_times(4)  #log statement. This will print hello 4 times

def print_hello_x_or_ten_times(x = 10): #declaring the function and inputing arguements in parameters.
    for num in range(x): 
        print('Hello')  #log statement

print_hello_x_or_ten_times()  #log statement 
print_hello_x_or_ten_times(4)  #log statement


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)