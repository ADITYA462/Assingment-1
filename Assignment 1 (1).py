#!/usr/bin/env python
# coding: utf-8

# Write a Python program to get the Fibonacci series between 0 to 50
# 
# 

# In[4]:


b,a=0,1

while b<50:
    print(b)
    b,a = a,a+b


# Write a Python program that accepts a word from the user and reverse it.
# 
# 

# In[2]:


def reverse(text):
    a = ""
    for i in range(1, len(text) + 1):
        a += text[len(text) - i]
    return a

print(reverse("Edyoda")) 


# Write a Python program to count the number of even and odd numbers from a series of numbers.
# 
# 

# In[3]:


num = (1,2,3,4,5,6,7,8,9)
even, odd= 0, 0

for i in num: 

    if i % 2 == 0: 

        even += 1

    else: 

        odd+= 1          

print("Number of Even numbers : ", even) 

print("Number of Odd numbers : ", odd)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




