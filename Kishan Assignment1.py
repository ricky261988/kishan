#!/usr/bin/env python
# coding: utf-8

# In[4]:


A=("Hello World")
A


# In[25]:


A= []
for i in range(2000,3200):
    if (i%7==0) and (i%5==0):
        A.append(str(i))
print (','.join(A))


# In[36]:


Name="Kishan Chaurasia"
print(Name[::-1])


# In[39]:


pi=3.14
r=6
V=4.0/3.0*pi* r**3
print(V)


# In[44]:


Value=input("Enter comma seperated number: ")
list= Value.split(",")
print('List: ',list)


# In[50]:


n=6;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[52]:


Word=input("InputWord: ")
for char in range(len(Word) -1,-1,-1):
    print(Word[char], end="")
print("\n")


# In[63]:


I= "WE, THE PEOPLE OF INDIA,{}having solemnly resolved to constitute India into a SOVEREIGN,{}SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC{}and to secure to all its citizens{}"
print(I.format('\n\t','!\n\t\t','\n\t\t',':'))


# In[ ]:




