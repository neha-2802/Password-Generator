import random
alphabets_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers_list=[0,1,2,3,4,5,6,7,8,9]
special_characters_list=['@','#','$','^','&','*']
size_of_password=int(input("Enter the size of password which you want:"))
no_of_alphabets=int(input("Enter the no. of alphabets:"))
no_of_numbers=int(input("Enter the no. of numbers:"))
no_of_specialcharacters=int(input("Enter the no. of special characters:"))
password_list=[]
for i in range(no_of_alphabets):
    c=random.choice(alphabets_list)
    password_list.append(c)
for j in range(no_of_numbers):
    n=random.choice(numbers_list)
    password_list.append(n)
for k in range(no_of_specialcharacters):
    s=random.choice(special_characters_list)
    password_list.append(s)
random.shuffle(password_list)
print("Your password is:",*password_list)

       
    
