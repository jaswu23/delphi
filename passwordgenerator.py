# Python password generator
# Author: Jason Wu
# Date: 29 April 2021



import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']


# get length of list
# get random number of length of list
# do x amount of times of list chosen

nr_letters = input("How many letters would you like in your password?\n")
nr_symbols = input("How many symbols would you like?\n")
nr_numbers = input("How many numbers would you like?\n")

num_letters = len(letters)
num_symbols = len(symbols)
num_numbers = len(numbers)


generated_password = ""



for x in range (0,int(nr_letters)):
    random_letter = letters[random.randint(0,num_letters-1)]
    generated_password += random_letter

for x in range (0,int(nr_symbols)):
    random_letter = symbols[random.randint(0,num_symbols-1)]
    generated_password += random_letter

for x in range (0,int(nr_numbers)):
    random_letter = numbers[random.randint(0,num_numbers-1)]
    generated_password += random_letter


#print("Password is:" + generated_password)
password_len = len(generated_password)
#print("Password Length:" + str(password_len))

random_position = (random.sample(range(0,password_len),password_len))
#print(x)
#print(len(x))

new_list = []
str = ""
for a in range (0, password_len):
    
    position = random_position[a]
    #print(str(a) + " " + generated_password[a] + " " + str(random_position[a]))
    new_list.insert(position,generated_password[a])


#print(new_list)


for e in new_list:
    str+=e

print("Your new password is: " + str)
    
