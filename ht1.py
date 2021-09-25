#!/usr/bin/env python
# coding: utf-8

# In[2]:


command = input ("Enter command:")
Dict = {"A": 'T', "C": 'G', "T": 'A', "G": "C", "a":"t", "c":"g", "t": "a", "g":"c"}
Dict_trans = {"A": 'U', "C": 'G', "T": 'A', "G": "C", "U":"A", "u":"a", "a":"u", "c":"g", "t": "a", "g":"c"}
m=[]
if command == "exit":
    print ("Good luck")
else:
    while True:
        sequence = input ("Enter sequence:")
        l= list(sequence)
        k2= ["U", "u"]
        k1= ["T", "t"]
        if all(x in Dict_trans for x in l) and not(any(item in k2 for item in l) and any(item in k1 for item in l)):    
            break
        else:
            print("Invalid alphabet. Try again!")
            
if command == "transcribe":
    for i in l:
        k = Dict_trans[i]
        m.append(k)
    j = ''.join(m)
    print (j) 
        
if command == "reverse":
    l2 = l[::-1]
    l3 = ''.join(l2)
    print (l3)
        
if command == "complement":
    for i in l:
        k = Dict[i]
        m.append(k)
    j = ''.join(m)
    print (j)
    
if command == "reverse complement":
    l2 = l[::-1]
    for i in l2:
        k = Dict[i]
        m.append(k)
    j = ''.join(m)
    print (j)        

