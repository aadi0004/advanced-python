#!/usr/bin/env python
# coding: utf-8

# In[1]:


# (1). Write a Python program to check if a number is even or odd using an if-else statement.
a=int(input("enter a number to check even or odd "))
if(a%2==0):
    print(a, "is even number")
else:
    print(a ,"is odd number")


# In[4]:


# (2). Write a Python program to check whether a given year is a leap year or not using conditional statements.
year=int(input("enter year "))
if (year%400 == 0) or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# In[6]:


# (3). Write a Python program to find the smallest of three numbers using if-elif-else.
a=int(input("enter value of a "))
b=int(input("enter value of b"))
c=int(input("enter value of c "))
if(a<b and a<c):
    print(f"{a} is smallest ")
elif(b<a and b<c):
    print(f"{b} is smallest ")
else:
    print(f"{c} is smallest")




# In[14]:


# (4). Write a Python program to determine if a character entered by the user is a vowel or consonant.
a=['aeiouAEIOU']
b=input("enter a characher ")
for i in a:
    if(b in i):
        print(f"{b} is vovel")
    else:
        print(f"{b} is consonant")


# In[19]:


# (5). Write a Python program to print the first 10 natural numbers using a while loop.
i=1
while(i<11):
    print(i)
    i+=1


# In[26]:


# (6). Write a Python program to calculate the factorial of a number using a for loop.
a=int(input("enter a num "))
fact=1
for i in range(1,a+1):
    fact=fact*i
print("factorial is", fact)



# In[27]:


# (7). Write a Python program to print all numbers from 1 to 100 that are divisible by 5 using a loop.
for i in range(1,100+1):
    if(i%5==0):
        print(i)


# In[7]:


# (8). Write a Python program to reverse the digits of a number using a while loop.
num=int(input("enter number "))
rem=0
sum=0
while(num>0):
    rem=num%10
    sum=sum*10 + rem
    num=num//10
    
print(f"reverse is {sum}")


# In[14]:


# (9).Write a Python program to count the number of occurrences of each vowel in a given string.
a=input("enter a string ")
count=0
for i in a:
    if(i.lower()=='a' or i.lower()=='e' or i.lower()=='i' or i.lower()=='o' or i.lower()=='u'):
        count=count+1
        
        
print(f"total vovels in {a} is {count}")


# In[17]:


# (10). Write a Python program to check whether a string is a palindrome or not.
a=input("enter string ")
b=a[::-1]
if(a==b):
    print("palindrome")
else:
    print("not palindrome")


# In[22]:


# (11). Write a Python program to find the length of a string without using the len() function.
a=input("enter string ")
count=0
for i in a:
    count=count+1
    
print(count)


# In[23]:


# (12). Write a Python program to find the frequency of a character in a string.
a=input("enter string ")
b=input("enter charchter to check frequency ")
count=0
for i in a:
    if(i==b):
        count=count+1
        
print(f"{b} in {a} is {count} times")


# In[25]:


# (13). Write a Python function to find the greatest of three numbers.
def greatest():
    a=int(input("enter value of a "))
    b=int(input("enter value of b "))
    c=int(input("enter value of c "))
    if(a>b and a>c):
        print(f"{a} is greatest ")
    elif(b>a and b>c):
        print(f"{b} is greatest ")
    else:
        print(f"{c} is greatest")
greatest()


# In[31]:


# (14). Write a Python function that takes a list of numbers as an argument and returns the sum of the numbers.
def sum1(li=[]):
    sum=0
    for i in li:
        sum=sum+i
    print(sum)
    
    
sum1([12,1,2,2])


# In[18]:


# (15). Write a Python function to check if a given number is a prime number or not.
def prime():
    a=int(input ("enter a number "))
    if(a>1):
        for i in range(2,a//2+1):
            if(a%i==0):
                print("not prime")
                break
        else:
                print("prime")
                
    else:
        print("not prime")
        
prime()


# In[ ]:




