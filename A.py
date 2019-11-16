#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import csv
from pprint import pprint
import time
import matplotlib.image as m
import matplotlib.pyplot as plt
import sys
sys.path.append(r"C:\Users\Batool\Desktop")
def Female_Palette_Color(I):
    
    with open("C:\\Users\\Batool\\Desktop\\Upskilling-Python\\chatbotProject\\Test.csv","r")as csvfile:
        reader=csv.reader(csvfile)
        header=next(reader)
        
        print("writing ....\n") ; time.sleep(2);A=input("How you choose your colors ?[Colors you like / no matter]\n")
        r=re.compile("\s*like\s*|\s*love\s*|\s*favorite\s*|\s*yes")
        if r.match(A)!=None:
            print("writing ....\n");time.sleep(2);print("Nice");time.sleep(2)
        else:
            print("writing ....") ; time.sleep(1);print("Nice"); time.sleep(2)
        print("writing ....\n") ; time.sleep(2);A=input("based on what you make colthes color matching ?[scientific/random]")
        if A=="scientific":
            print("writing ....") ; time.sleep(2);X=input("How ? ")
            r=re.compile("color\s+palette")
            if r.match(X)!=None:
                print("Perfect")
        elif A=="random":
            print("writing ....") ; time.sleep(2);X=input("How ? ")
            print("writing ....") ; time.sleep(2);print("You should use color palette")
            
        print("writing ....\n") ; time.sleep(1);print(I+" Are you ready to be Awesome ! "+"\n so tell me "+I+" what's your baisc color today ?\n",header)
        Basic_Color=input()
#-----------------------------------------------------------------------------------------------------          
        Reg=re.compile("r|R\w*")
        R1=Reg.match(Basic_Color)
        if Basic_Color.lower()=="red" or R1!=None:
            print("writing ....\n") ; time.sleep(2);print("Nice color , you can make a color collection form these options\n ")
            for row in reader:
                print("writing ....\n") ;time.sleep(2);print(row[0])
                img = m.imread('C:\\Users\\Batool\\Desktop\\Upskilling-Python\\chatbotProject\\R\\1.jpg') 
                plt.imshow(img) 
#-----------------------------------------------------------------------------------------------------  
        Reg=re.compile("g|G\w*")
        R1=Reg.match(Basic_Color)
        if Basic_Color.lower()=="green" or R1!=None:
            print("writing ....\n") ; time.sleep(2)
            print("Nice color , you can make a color collection form these options\n ")
            for row in reader:
                print("writing ....\n") ;time.sleep(2);print(row[1])
#             print("writing ....\n") ; time.sleep(1)
            img = m.imread('C:\\Users\\Batool\\Desktop\\Upskilling-Python\\chatbotProject\\G\\2.jpg') 
            plt.imshow(img) 
#-----------------------------------------------------------------------------------------------------  
        Reg=re.compile("b|B\w*")
        R1=Reg.match(Basic_Color)
        if Basic_Color.lower()=="blue"or R1!=None:
            print("writing ....\n") ; time.sleep(1); print("Nice color , you can make a color collection form these options\n ")
            for row in reader:
                print("writing ....\n") ;time.sleep(1) ; print(row[2])
            img = m.imread('C:\\Users\\Batool\\Desktop\\Upskilling-Python\\chatbotProject\\B\\3.jpg') 
            plt.imshow(img)
#-----------------------------------------------------------------------------------------------------            
        Reg=re.compile("y|Y\w*")
        R1=Reg.match(Basic_Color)
        if Basic_Color.lower()=="yellow" or R1!=None:
            print("writing ....\n") ; time.sleep(1);print("Nice color , you can make a color collection form these options\n ")
            for row in reader:
                print("writing ....\n") ;time.sleep(1) ; print(row[3])
            img = m.imread('C:\\Users\\Batool\\Desktop\\Upskilling-Python\\chatbotProject\\Y\\6.jpg') 
            plt.imshow(img)
#-----------------------------------------------------------------------------------------------------              
        Reg=re.compile("p|P\w*")
        R1=Reg.match(Basic_Color)
        if Basic_Color.lower()=="purple"or R1!=None:
            print("writing ....\n") ; time.sleep(1);print("Nice color , you can make a color collection form these options\n ")
            for row in reader:
                print("writing ....\n") ;time.sleep(1) ; print(row[4])
            img = m.imread('C:\\Users\\Batool\\Desktop\\Upskilling-Python\\chatbotProject\\P\\4.jpg') 
            plt.imshow(img)
#-----------------------------------------------------------------------------------------------------              
        Reg=re.compile("o|O\w*")
        R1=Reg.match(Basic_Color)    
        if Basic_Color.lower()=="orange"or R1!=None:
            print("writing ....\n") ; time.sleep(1);print("Nice color , you can make a color collection form these options\n ")
            for row in reader:
                print("writing ....\n");time.sleep(1) ; print(row[5])
            img = m.imread('C:\\Users\\Batool\\Desktop\\Upskilling-Python\\chatbotProject\\O\\4.jpg') 
            plt.imshow(img) 
#-----------------------------------------------------------------------------------------------------          
        Reg=re.compile("i|I\w*")
        R1=Reg.match(Basic_Color)
        if Basic_Color.lower()=="indigo"or R1!=None:
            print("writing ....\n") ; time.sleep(1);print("Nice color , you can make a color collection form these options\n ")
            for row in reader:
                time.sleep(1) ; print(row[6])
            img = m.imread('C:\\Users\\Batool\\Desktop\\Upskilling-Python\\chatbotProject\\I\\4.jpg') 
            plt.imshow(img)      
        print("writing ....\n") ;time.sleep(2);A=input("Which option you chooes ?\n");print("writing ....\n") ; time.sleep(2);print("Nice one\n")
        print("writing ....\n") ; time.sleep(2);A=input("The options was enough ?\n")
        if A=="no"or A=="No" or A=="NO":print("for more press the link : https://stock.adobe.com")
        print("writing ....\n") ; time.sleep(2);A=input("Tell me what is a color palette ?\n");print("writing ....\n") ; time.sleep(2);print("Color palette refers to particular combination of colors\n"); time.sleep(2)
        print("writing ....\n") ; time.sleep(2);B=input("are going to use color palette ?\n")
        if B=="yes":
            print("writing ....\n");time.sleep(2);print("Thats perfect")
        elif B=="no":
            print("writing ....\n");time.sleep(2);print("Try to use it ,It will help you alot");time.sleep(2)
        print("writing ....\n");time.sleep(2);A=input("can you tell me anything about colors ?")

        
        
        
        
        
        
        
        
        
def Occasion(In):
        li=["party","dinner","work",'sport']
        Occ=input ("what is your occasion ?\n[party,dinner,work,sport]\n")
        if Occ==li[0]:
            print("writing ....\n") ; time.sleep(1);Oc2=input("is it indoor or outdoor ?");print("writing ...") ; time.sleep(1);print("Have fun\n");Oc3=input("you prefer to wear in formal way in general ? \n");input();print("writing ....") ; time.sleep(1);print("I prefer casual");print("writing ....\n") ; time.sleep(1);
            print("writing ....\n") ; time.sleep(1);Oc4=input("do you prefer this kind of occasion ? or you Prefer different type? ");print("writing ....") ; time.sleep(1)
            print("writing ....\n") ; time.sleep(1);Oc1=input("Nice Enjoy "+In+" you will wear dress or skirt ? ")
            print("writing ....\n") ; time.sleep(1);input("It think is better to wear a dress,what do you think ? ")
            print("writing ....");time.sleep(1); print("Cool")
            print("writing ....");time.sleep(1); Oc6=input("every thing is ok untill now ? [yes/No] \n")
            if Oc6=="yes":
                print("writing ....");time.sleep(1);print("lets play and have fun\n")
#                 Game()
            elif Oc6=="no":
                print("writing ....");time.sleep(1);print("lets play and have fun\n")
#                 Game()
            
        if Occ==li[1]:
            Oc1=input("is it indoor or outdoor ?\n");print("writing ....\n") ; time.sleep(1);print("Have fun");print("writing ....\n") ; time.sleep(1);Oc3=input("you prefer to wear in formal way in general ? \n");input();print("writing ....") ; time.sleep(1);print("I prefer casual \n")
            print("writing ....\n") ; time.sleep(1);Oc4=input("do prefer this kind of occasion ? or you Prefer different type ? \n");print("writing ....\n");time.sleep(1)
            print("writing ....\n") ; time.sleep(1);Oc12=input("Tts dinner time "+In+"a business or family dinner ? \n")
            print("writing ....\n") ; time.sleep(1);Oc2=input("so today you will wear dress or casual ? \n")
            print("writing ....\n") ; time.sleep(1);input("It think is better to wear formal in business dinner,what do you think ? \n")
            print("writing ....\n");time.sleep(1); print("Cool")
            print("writing ....\n");time.sleep(1); Oc6=input("every thing is ok untill now ? [yes/No] \n")
            if Oc6=="yes":
                print("writing ....");time.sleep(1);print("lets play and have fun\n")
#                 Game()
            elif Oc6=="no":
                print("writing ....");time.sleep(1);print("lets play and have fun\n")
#                 Game()
        if Occ==li[2]:
            Oc1=input("is it office or outoffice ?");print("writing ....\n") ; time.sleep(1);print("Have fun");Oc3=input("you prefer to wear in formal way in general ? ");input();print("writing ....\n") ; time.sleep(1);print("I prefer casual")
            print("writing ....\n") ; time.sleep(1);Oc4=input("do prefer this kind of occasion ? or you Prefer different type? ");print("writing ....\n") ; time.sleep(1)
            print("writing ....\n") ; time.sleep(1);Oc12=input("Its work time "+In+" casual or Jeans? \n")
            print("writing ....\n") ; time.sleep(1);input("Any of them is good,what do you think ? \n")
            print("writing ....");time.sleep(1); print("Cool")
            print("writing ....");time.sleep(1); Oc6=input("every thing is ok untill now ?[yes/No] \n")
            if Oc6=="yes":
                print("writing ....");time.sleep(1);print("lets play and have fun\n")
#                 Game()
            elif Oc6=="no":
                print("writing ....");time.sleep(1);print("lets play and have fun\n")
#                 Game()
        if Occ==li[3]:
            Oc1=input("is it office or outoffice ?");print("writing ....\n") ; time.sleep(1);Oc4=input("do prefer this kind of occasion ? or you Prefer different type ? \n");print("writing ....\n") ; time.sleep(1)
            print("writing ....\n") ; time.sleep(1);Oc12=input("123 Healthy life yes ! "+In+" so adidas ? \n")
            print("writing ....\n") ; time.sleep(1);input("The most Important is comfortability,Right ? \n")
            print("writing ....\n") ; time.sleep(1)
            input("what you are going to wear ?\n")
            print("writing ....");time.sleep(1); print("Cool");print("writing ....\n") ; time.sleep(1);Oc3=input("you prefer to wear in formal way in general? \n")
            print("writing ....");time.sleep(1); Oc6=input("every thing is ok untill now ? [yes/No]\n")
            if Oc6=="yes":
                print("writing ....");time.sleep(1);print("lets play and have fun\n")
#                 Game()
            elif Oc6=="no":
                print("writing ....");time.sleep(1);print("lets play and have fun\n")
#                 Game()


# In[ ]:




