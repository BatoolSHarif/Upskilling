#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x=input("Insert string : ")
f=int(x)
print(type(x))
print(type(f))


# In[ ]:


x=input("Enter the first number:")
y=input("Enter the second number:")
print(x,y)


# In[ ]:


p=input("Enter a number :")
p=int(p)
q=p/3
if q==1 :
    print ("devisable")
else:
    print("Not divisable")    


# In[ ]:


a=input("Enter the first number:")
b=input("Enter the second number:")
c=input("Enter the third number:")
a=int(a)
b=int(b)
c=int(c)

x=(-b+c**4)/(2*a)
xx=(3*(a+b**2))/c
x1=x-xx
print(int(x))
print(int(xx))
print("The value of X1 = ",int(x1))

x2=((a+b**3)**2)/(c-a**2)
print("The value of X2 = ",int(x2))


# In[ ]:


a=input("Enter the first number:")
b=input("Enter the second number:")
print (max(int(a),int(b)))


# In[ ]:


a=input("Enter the first number:")
b=input("Enter the second number:")
c=input("Enter the third number:") 
a=int(a)
b=int(b)
c=int(c)

print("The Maximum Number  Is : ",max(a,b,c))


# In[ ]:


a=input("Enter the first number:")
b=input("Enter the second number:")
b=int(b)
a=int(a)
if b==0:
    print ('"b is 0"')
else:
    print (int(b*(a/b)))


# In[15]:


a=input("Enter the number of days:")
a=int(a)
year = int(a/365)
month=a/30
day=a
print ("The number of Years : ",year)
print ("The number of month : ",month)
print ("The number of days : ",abs((year*365)-(month*30)))


# In[ ]:


a=int(input("Enter the temperature in Celsius:"))
int(a)
a=(a*(9/5))+32
print ("The temperature in Fahrenheit is = ",a," F")


# In[ ]:


x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
(x**2-y**2)=(x-y)
z=


# In[ ]:


a=input("Enter your r Q-Range (”deviation IQ”):")
a=int(a)
if a>= 130:
    print ("Very Superior")
else:
    if a>=120 and a<=129:
        print ("Superior")
    else:
        if a>=110 and a<=119:
            print ("High Average")
        else:
            if a>=90 and a<=109:
                print ("Average")
            else:
                if a>=80 and a<=89:
                    print ('Low Average')
                else:
                    if a>=70 and a<=79:
                        print (' Borderline')
                    else:
                     if a<=69:
                        print ('Extremely Low')


# In[ ]:


a=input("Enter your Grade Please :")
a=int(a)
if a>= 90 and a<=100:
    print ("[90-100] : A")
else:
    if a>=80 and a<90:
        print ("[80-90] : B")
    else:
        if a>=70 and a<80:
            print ("[70-80] : C")
        else:
            if a>=60 and a<70:
                print ("[60-70] : D")
            else:
                if a>=50 and a<60:
                    print ('[50-60] : E')
                else:
                    if a>=0 and a<50:
                        print (' [0-50] : F')


# In[ ]:


a=input("Enter the first number:")
b=input("Enter the second number:")
c=input("Enter the third number:") 
a=int(a)
b=int(b)
c=int(c)

sum=a**2+b**2
if sum ==c**2:
    print ("They Are Equal")
else:
    print ("They Are not Equal according to this Equaion 'a^2 + b^2 =c^2'")


# In[ ]:


a=input("Enter an alphabet:")
v='a,A,o,O,u,U,i,I,e,E'
if a in v:
    print ("the alphabet "+a+" is Vowel")
else:
    print ("the alphabet "+a+" is Consonant")
    


# In[ ]:


a=input("Enter a number:")
a=int(a)
if a/2 ==0:
    print ("Is an Odd Number")
else:
    print ("Is an Even Number")


# In[ ]:


from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
print("Current date and time =", dt_string)	


# In[ ]:


import math
r=float(input("Enter the raduis: "))
print("r =",r)
print ("Area = ",math.pi*r**2 ," m2")


# In[ ]:


name=input("Enter your first and Last name : ")
print ("Reverse Name :",list(reversed(name)))


# In[18]:


a=input("(")
b=input("")
c=input("")
print()
a=int(a)
b=int(b)
c=int(c)

print("The examination will start from",a,"/",b,"/",c)


# In[19]:


n=int(input("Enter a number:"))
num= (n+ ((n*10)+n) + ((n*100)+(n*10)+n))
print("Sample value of n is",n )
print("Expected Result :",num )


# In[20]:


print(abs.__doc__)


# In[20]:


from datetime import date
import math
date1=date(2014,7,2)
date2=date(2014,7,11)
dd=date1-date2
print(abs(dd.days))


# In[22]:


import math
r=float(input("Enter the raduis: "))
print("r =",r)
print ("Area = ",(4/3)*math.pi*r**3 ," m3")


# In[26]:


num=int(input("Enter a number : "))
if num>17:
    absDouble=(abs(17-num))**2
    print(absDouble)
else:
    print(17-num)


# In[3]:


num=int(input("Enter a Number : "))
if num<100 or num<1000 or num<2000:
    print((num/5)*25)
else:
    print("Greater than 100 or 1000 or 2000")


# In[4]:


a=input("Enter the first number:")
b=input("Enter the second number:")
c=input("Enter the third number:") 
a=int(a)
b=int(b)
c=int(c)

sum=a+b+c
if a==b and a==c and b==c:
    print ("They Are Equal")
    print (sum**3)
else:
    print ("They Are not Equal")
    print(sum)


# In[9]:


a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
asw=b
bsw=a
print("The Swaped Value of",a,"is",": ",asw)
print("The Swaped Value of",b,"is",": ",bsw)


# In[10]:


L1=int(input("Enter a Number : "))
List=[1,5,8,3]
if L1 in List :
    print(L1,"->",List,"True")
else:
    print(L1,"->",List,"False")


# In[12]:


base=int(input("Enter Base:"))
hight=int(input("Enter hight:"))
print("The Area Of The Triangel = ",(1/2)*base*hight)


# In[15]:


a=input("Enter the first number:")
b=input("Enter the second number:")
c=input("Enter the third number:") 
a=int(a)
b=int(b)
c=int(c)

sum=a+b+c
if a==b or a==c or b==c:
    print ("They Are Equal")
    sum=0
    print ("sum= ",sum)
else:
    print ("They Are not Equal")
    print(sum)


# In[21]:


a=input("Enter the first number:")
b=input("Enter the second number:")
a=int(a)
b=int(b)
sum=a+b
if sum>=15 and sum<=20:
    print ("sum= ",20)
else:
    if sum>=30 and sum<=40:
        print ("sum= ",50)
    else:
        if sum>=150 and sum<=167:
            print ("sum= ",210)
        else:
            print(sum)


# In[29]:


a=input("Enter the first number:")
b=input("Enter the second number:")
a=int(a)
b=int(b)
if a==b or a+b==5 or abs(a-b)==5:
    print (a==b)
else:
    print(a==b)


# In[32]:


x=input("Enter the first number:")
y=input("Enter the second number:")
x=int(x)
y=int(y)

sol=(x+y)*(x+y)
print("((",x,"+",y,")**2)= ",sol)


# In[2]:


import math
x1,y1=input("Enter X1 , Y1 : ").split()
x2,y2=input("Enter X2 , Y2 : ").split()
x1=int(x1)
y1=int(y1)
x2=int(x2)
y2=int(y2)

dis=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print("The disctance btween 2 Points = ",dis)


# In[4]:


help(sum)


# In[ ]:


print ("Insert 1 for feet or 2 for Inches : ")
choose=int(input())
if choose==1:
    x=input("Enter the hight in feet :")
    x=int(x)
    print("The FeetHight in centimeters = ",x*30.48," cm")
else:
    y=input("Enter the hight Inches : ")
    y=int(y)
    print("The InchesHight in centimeters = ",y*2.54," cm")


# In[ ]:


import math
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
hypotenuse =math.sqrt((a**2+b**2)) 
print("The hypotenuse = ",hypotenuse)


# In[10]:


print ("Insert 1 for Inches or 2 for yards or 3 for miles : ")
choose=int(input())
if choose==1:
    x=input("Enter the distance in feet :")
    x=int(x)
    print("The FeetDistances in Inches = ",x*12," Inche")
else:
    if  choose==2:
        y=input("Enter the Distances in Feet : ")
        y=int(y)
        print("The Distances in Yards = ",y*0.33333," yards")
    else:
        if choose==3:
            z=input("Enter the Distances in Feet : ")
            z=int(z)
            print("The Distances in miles = ",z* 0.00018939," mile")


# In[16]:


mins=int(input("Enter min :"))
days=mins/1440
month = mins/34200
year = mins/518400
print("Days = ",days)
print("Moths = ",month)
print("Years= ",year)


# In[18]:


year=int(input("Enter years :"))
days=year*365
month = year*12
print("Days = ",days)
print("Moths = ",month)


# In[3]:


height=float(input("Enter height :"))
Weight=float(input("Enter Weight :"))
mass=Weight/(height*height)
print("your body Mass index is= ",mass)


# In[25]:


l=[2,8,3,0,8]
print (l)
l2=sorted(l)
print ("The Sorted Numbers :",l2)


# In[27]:


import math            
math_ls = dir(math) 
print(math_ls)


# In[ ]:


char=input("Enter char to get its ASCII code :")
print("The ASII code for ",char,"is",ord(char))


# In[ ]:





# In[ ]:





# In[ ]:


str1=input("Enter String 1 :")
str2=input("Enter String 2:")
str3=input("Enter String 3 :")
str4=input("Enter String 4 :")
print(str1+str2+str3+str4)


# In[6]:


str1=input("Enter any String :")
T=str1.isnumeric()
print(T)


# In[11]:


x=int(input("Enter num :"))
print("Hello :")
if x==1:
    set.clear()


# In[15]:


x=int(input("Enter num :"))
if x>0:
    print("The number :",x,"is Positive")
else:
    if x<0:
        print("The number :",x,"is Negative")
    else:
        if x==0:
            print("The number :",x,"is Zero")


        

    


# In[35]:


x = input ("Enter a number")
try:
   val = int(x)
   print("Yes input string ",val," is an Integer.")
except ValueError:
   print("That's not an int!")


# In[14]:


str1="python"      
str2="python"
ID1=hex(id(str1))
ID2=hex(id(str2))
print("Str1 MemLocation: ",hex(id(str1)),'\n',"Str2 MemLocation: ",hex(id(str2)))


# In[17]:


str1=input("Enter String 1 :")   
str2=input("Enter String 2:")
if str1==str2:
    print("Same Strings!")
else:
    print("Not the same strings !")


# In[19]:


num=int(input("Enter number :"))     
print("num = ",num)
    


# In[24]:


str1=input("Enter String 1 :")           
print(str1.islower())


# In[ ]:


str1=input("Enter String 1 :")
print("Original String: ",str1)
str1 = str1.ljust(8, '0')
print("After Extinding :",str1)


# In[ ]:





# In[6]:


num=int(input("Enter number :"))
print("Original String: ",bnum)
print("After Extinding :",format(num,'08b'))


# In[13]:


x,y=input("Enter x and y numbers :").split(",")
print("The Value of x is :",int((x)),"\n","The Value of y is :",int(y))


# In[16]:


d=int(input("Enter number :"))
print("d= ",d)
h=hex(d)
print("h= ",h)


# In[8]:


x,y,z,g,h=input("Enter 5 numbers :").split(",")
x=int(x)
y=int(y)
z=int(z)
g=int(g)
h=int(h)
maxi=0
mini=0
print("For Max Enter 1  For min Enter 2 :")
t=int(input())
if t==1:
    if x>y and x>z and x>g and x>h:
        maxi=x
        print("Max =",maxi)
    else:
        if y>x and y>z and y>g and y>h:
            maxi=y
            print("Max =",maxi)
        else:
            if z>x and z>y and z>g and z>h:
                maxi=z
                print("Max =",maxi)
            else:
                if g>x and g>z and g>y and g>h:
                    maxi=g
                    print("Max =",maxi)
                else:
                    if h>x and h>z and h>g and h>y:
                        maxi=h
                        print("Max =",maxi)
                    else:
                        print("Equal mnubers!")
else:
    if x<y and x<z and x<g and x<h:
        maxi=x
        print("Max =",maxi)
    else:
        if y<x and y<z and y<g and y<h:
            maxi=y
            print("Max =",maxi)
        else:
            if z<x and z<y and z<g and z<h:
                maxi=z
                print("Max =",maxi)
            else:
                if g<x and g<z and g<y and g<h:
                    maxi=g
                    print("Max =",maxi)
                else:
                    if h<x and h<z and h<g and h<y:
                        maxi=h
                        print("Max =",maxi)
                    else:
                        print("Equal mnubers!")

