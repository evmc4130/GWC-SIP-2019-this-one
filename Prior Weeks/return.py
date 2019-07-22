#MORE PRACTICE WITH FUNCTIONS

def stringToList(string1):
    if(type(string1) == str):
        listReturned = []
        for i in string1:   #can also be for i in range(0,len(string1)): #<-- I want us to play with range(0,6)
            listReturned.append(i) #this automatically alters list returned
        return listReturned

def fruitsSquashed(fruit1,fruit2):
    if(type(fruit1) == str and type(fruit2) == str):
        combined = fruit1+fruit2
        #print(combined)
        return combined

izearsFruit = "strawberry" #string type
marielasFruit = "peach"

pink = stringToList(izearsFruit)
print(pink)
#stringToList(izearsFruit)
#var = fruitsSquashed(izearsFruit, marielasFruit)
#print(var)

#fruitsSquashed("strawberry", "peach")
orange = fruitsSquashed(mariel)


#print(counter)
# a  = stringToList("hello")
# print(a[6])



#stringToList("hellos")

#print(a)
