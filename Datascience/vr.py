#name1 = "akshaya"
#print(name1)
#age = 20
#print(age)
#print(type(age))
#print(type(name1))
#print(float(age))
#var1 = "23442"
#var2 = float(var1)
#print(var2)

#num1 = int(input("Enter a num"))
#if num1 > 0:
 #   print("positive")
#elif num1 == 0:
 #   print("Zero")
#else:
 #   print("Neg")

#num2 = int(input("Enter a num"))
#if num2 % 2 ==0:
 #   print("even")
#else:
 #   print("odd")

#for i in range(1,51,3):
 #   print(i)

#for i in range(1,21):
 #   if i % 2 ==0:
  #      print(i)

#LIST

#l = ["apple","mango","cherry"]
#for i in l:
 #   print(i)

#print(l[0:2])   

#n =8
#n7=str(n)
#print(n7)
#print(type(n7))

#i = 0
#while i < 10:
 #   print(i)
  #  if i == 5:
   #     break

    #i += 1

#i = 0
#while i < 10:
 #   if i == 5:
  #      continue
   # print(i)
    #i += 1

#FUNCTIONS
#def add(a,b):
 #   c=a+b
  #  print("Sum=",c)
#add(a=6,b=10)

#MERGING NAME
#def add(a,b):
 #   print("First name:",a)
  #  print("Last name:",b)
#add(a="Akshaya",b="G")

#KEYWORD ARG
#def greet(name,age):
 #   print(name,age)
#greet(age=20,name="Akshaya")

#POSITIONAL ARG
#def greet(name,age):
 #   print(name,age)
#greet("Akshaya",20)

#LIST (MUTABLE)
#l1=["apple","orange","cherry"]
#l1[1]="grapes"
#print(l1)

#TUPLE (IMMUTABLE)
#x=("hey","hi","hello")
#y=list(x)
#y.remove("hi")
#x=tuple(y)
#print(x)

#DICTIONARY
#d = {"brand":"ford",
 #    "model":"mustang",
  #   "year":1964}
#print(d)
#print(d["brand"])

#d = {"brand":"ford",
 #    "model":"mustang",
  #   "year":2009,
   #  "year":1964} # doent allow duplicate if it exist it returns the last val

#print(d)

d1={"name":"akshaya",
     "age":20,
    "age":21,
    "college":"MAMS"}
#print(d1)

#To get keys only
#x=d1.keys()
#print(x)

#To get values only
#y=d1.values()
#print(y)

#To get both keys and val
#z=d1.items()
#print(z)

#Changing val of a particular key
#["name"]="Lily"
#print(d1)

#OR use update for inserting new keyval pair orupdate any key
#d1.update({"year":2024})
#d1.update({"age":40})
#print(d1)


#delete the last item
#d1.popitem()
#print(d1)

#delete a particular item
#d1.pop("name")
#print(d1)

#del keyword can also delete the dict completely

#del d1
#print(d1) #o/p error

#return an empty dict this clear() empties the dict
#d1.clear()
#print(d1)

#Loop for key
#for x in d1:
 #   print(x)

#Loop for keys only
#for x in d1.keys():
 #   print(x)

#loop for values only
#for x in d1.values():
#    print(x)

#loop for both key val
#for x,y in d1.items():
 #   print(x,y)

 d1 = "name":{
       "age":20,
       "yr":309},
"name1":{
 "age1":23,
 "yr1":456}