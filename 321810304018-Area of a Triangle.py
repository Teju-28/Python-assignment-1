#!/usr/bin/env python
# coding: utf-8

# ## Area of a Triangle 

# In[1]:


# Three sides of a triangle a,b and c:
a = float(input('Enter first side:'))
b = float(input('Enter second side:'))
c = float(input('Enter third side:'))
#Calculate Semi-perimeter
s = (a+b+c)/2
#Calculate Area
area = (s*(s-a)*(s-b)*(s-c))**0.5
print('The area of a triangle is %.2f' %area)


# In[ ]:




