#!/usr/bin/env python
# coding: utf-8

# In[22]:


try:
    c = int(input("Enter Celcium degrees "))
    task = input("Enter degrees to convert: Fa, K ")
    if task == "Fa":
        f = (c*9/5) + 32
        print(f)
    elif task == "K":
        k = c+273
        print(k)
    else:
        print("Wrong input")
except ValueError:
    print("You have typed wrong data")

