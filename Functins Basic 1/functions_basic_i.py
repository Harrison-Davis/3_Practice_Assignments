#1      will print 5
def number_of_food_groups():
    return 5
print(number_of_food_groups())


#2      will print an error because  "number_of_days_in_a_week_silicon_or_triangle_sides()" is not defined
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


#3      will print 5
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())


#4      will print 5
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())


#5      will print 5, none
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)


#6      will print 8   ---->  did not print becuase + should have been a comma
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))


#7      will print "25"
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))


#8      will print 100 10
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9      will print 7   14    21
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10     8
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11    .will print   500    300     300    300    300
#------> 500     500     300     300 
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12     will print    500   500   300   500  
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13     500     500     b=300      500
#-----> 500     500     300     300
#confused on this one.

b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14     will print      1      2       3
#----->   1     3       2
#confused on this one
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15     wlll print      1   3       5       10
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)