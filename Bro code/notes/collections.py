# list = [] ordered , changeable , dupes allow
# set = {}  unordered ,  immutable(can add or remove tho) , dupes not allow
# tuple = () ordered , unchangeable , dupes ok          [faster]

fruits = ["apple" , "orange" , "banana" ,"coconut"]
#           0         1           2          3
#print(fruits[4]) will be a index out of range error

# can in iterated in loops
for fruit in fruits:
    print(fruit)
# list methods   # when u have element use remove when u have index use pop
print(dir(fruits)) # gives the list of possible methods of this list 
print(help(fruits)) # gives the list and description of those methods
print(len(fruits)) # gives the length of the list 
print("apple" in fruits) # gives the boolean of that condition
fruit[4] = "peach" # add element to a certain position will change the prev value too
# fruits.append("peach") -> adds element to the end of the list
# fruits.remove("peach") -> removes the element
# fruits.insert(0 , "peach") - > insert this elemend in that position and pushes the others back
# fruits.sort() -> alpha order
# fruits.reverse() -> reverse whatever order the list is in (for reverse alpha first sort it)
# fruits.clear() -> empty a list
# fruits.index("apple") -> gives the position
# fruits.count("Banana") -> num of dupes in list

# set methods
fruits = {"apple" , "orange" , "banana" ,"coconut"} #- > no order
# fruits.add("peach") 
# fruits.remove("peach")
# fruits.pop() -> gives a random element from the list 
print(dir(fruits)) # gives the list of possible methods of this list 
print(help(fruits)) # gives the list and description of those methods
print(len(fruits)) # gives the length of the list 
# tuple methods 
fruits =("apple" , "orange" , "banana" ,"coconut") # ordered and unchageable (faster than lists)
print(dir(fruits)) # gives the list of possible methods of this list 
print(help(fruits)) # gives the list and description of those methods
print(len(fruits)) # gives the length of the list 
# only .index() and .count() works

# 2d collections 

fruits = ["apples" , "oranges" , 'peach' , 'kiwi']
vegetable = [ 'cauliflower' , 'carrot' , 'radish' ]
meat = [ 'beef' , 'pork' , 'chicken' , 'mutton' , 'lamb'] 
food = [ fruits , vegetable , meat ] # or food = [ ["apples" , "oranges" , 'peach' , 'kiwi'],
#                                                  [ 'cauliflower' , 'carrot' , 'radish' ],                                        
#                                                  [ 'beef' , 'pork' , 'chicken' , 'mutton' , 'lamb']]
# print( food[0][3])  = 'kiwi'


# Dictionary methods 
capitals = { 
"Nepal" : "Kathmandu",
"USA"   : "Washington DC",
"India" : "New Delhi" ,
"Russia" : "Moscow" 
} # the first one is key and the second is value
# print(dir(capitals)) - > all the methods of the dictionary 
# print(help(capitials)) - > their description

capitals.get("USA") # -> gives the value of the keyword if it dose not have it returns none ( can be used in if else to )
capitals.update({"Germany" , "Berlin"}) # adds value
capitals.pop("India") # removes this element 
capitals.keys() # gives the keys of the dictionary
for key in capitals.key() :
    pass
values = capitals.values() # same thing 
print(values)
items = capitals.itmes()
for key , value in capitals.items(): # prints out the dictionary
    pass
