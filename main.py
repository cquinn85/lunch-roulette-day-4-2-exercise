import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Get the total number of items in list
items = len(names)

#Generate random numbers between 0 and the last index.
rando_num = random.randint(0,items - 1)

#Pick out random person from list of names using the random number.
person_who_will_pay = names[rando_num]

print(person_who_will_pay + " will pay for the meal!")


