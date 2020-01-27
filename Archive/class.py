# greeting = " Hello {}, it is very nice to meet you and your friend {}"

# name_of_user = input("What is your name?")
# length_of_name = len(name_of_user)
# if length_of_name > 0:
#     name_of_friend = input("what is your friend's name?")
#     print(greeting.format(name_of_user, name_of_friend) )
# elif length_of_name == 0:
#     name_of_friend = input("Ok fine, how about your friend's name?")
#     print(greeting.format("john doe", name_of_friend) )
# else:
#     print("ok, I'll ask again some other time.")




#WEDNESDAY 1/15






# day1 = "Sunday"
# day2 = "Monday"
# day3 = "Tuesday"
# day4 = "Wednesday"
# day5 = "Thursday"
# day6 = "Friday"
# day7 = "Saturday"

# days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# day 1 = days[0]
# print(day 1)

# number = [1, 2, 3, 4, 5]

# print(number [1])

# print(len(number))

# number[0] = 23
# print(number[0])
# number.append(9)
# print(number)

# todos = ["pet the cat", "go to work", "shop for groceries", 
# "go home", "feed the cat"]
# todos.append("binge watch a show")
# todos.append("go to sleep")
# print(todos)

# count = 0

# while count < len(todos):
#     print(f"{count}: {todos[count]}")
#     count += 1

# todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]
# del todos[0] # Remove the first one
# print(todos)
# del todos[1:3] # Remove items at index 1 up but not including index 3
# print(todos)

# todos = []
# item = input("Add item?")

# while len(item) > 0:
#     todos.append(item)
#     print(todos)
#     item = input("Add item?")
# print(todos)

# for num in range(1,1001,2):
#     print(num)

# for a in range(1,11):
#     print("...")
#     for b in range(1,11):
#         c = a * b
#         print (a, "x", b, "=", c)

# count = 0
# while count < 3:
#     print('Hello')
#     count += 1

# for r in range(3):
#     print('Hello')







#THURSDAY 1-16-19








# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for letter in alphabet:
#     print(letter)
# r = 0
# for x in range(1,11):
#     r += 1
#     s = (x) * (x)
#     print(f"{r} = {s}")

# week = ["Week 1", "Week 2", "Week 3", "Week 4"]
# day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# todo = ["lecture", "HW", "solutions"]

# for w in week:
#     print(w)
#     for d in day:
#         print(f' {d}')

# def greeting():
#     print("Hello world")

# def greeting(person):
#     print(f'Hello {person}!')
# greeting('Steven')

# def add(num1, num2):
#     sum = num1 + num2
#     return sum

# result = add(4, 5)
# print(result)

# def cal_avg(p1, p2, p3, p4):
#     sum = p1 + p2 + p3 + p4
#     avg = sum/4
#     return avg
# result = cal_avg(4, 6, 9, 0)
# print(result)
# li = input("Enter values:")
# li2 = list(li)

# def cal_avg(li2):
#     l = len(li2)
#     sum = 0
#     for i in li2:
#         sum += i
#     average = sum/l
#     return average
# TAX_RATE = .09  # 9 percent tax
# COST_PER_SMALL_WIDGET = 5.00
# COST_PER_LARGE_WIDGET = 8.00
# def calculateCost(nSmallWidgets, nLargeWidgets):
#     subTotal = (nSmallWidgets * COST_PER_SMALL_WIDGET) + (nLargeWidgets * COST_PER_LARGE_WIDGET)
#     taxAmount = subTotal * TAX_RATE
#     totalCost = subTotal + taxAmount
#     return totalCost
# total1 = calculateCost(4, 8)  #  4 small and 8 large widgets
# print('Total for first order is', total1)
# total2 = calculateCost(12, 15)







#FRIDAY 1/17




# my_dictionary = {
#     "hello" : "world",
#     "square_of_2" : 4,
#     0 : 1}

# # print(my_dictionary["hello"])
# # print(my_dictionary[0])

# for k,v in my_dictionary.items():
#     print(f'{k} {v}')

# contacts = [{
#     "First_name" : "Veronica",
#     "last_name" : "Lino"},
#     {
#     "First_name" : "Sean",
#     "Last_name" : "Page",
#     "Phone" : "33030303030"},
#     {"First_name" : "Steven",
#     "Last_name" : "Johnson"}]

# #print(contacts[1])
# print(contacts[1]["First_name"], contacts[1]["Last_name"], contacts[1]["Phone"])







#Monday 1/27




from random import choice

places = ["Wendy's", "KFC", "Burger King", "Taco Bell"]

def pick():
    return choice(places)

print(pick())
print(pick())


