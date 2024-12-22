# list = [] ordered , changeable , dupes allow
# set = {}  unordered ,  immutable(can add or remove tho) , dupes not allow
# tuple = () ordered , unchangeable , dupes ok          [faster]

fruits = ["apple" , "orange" , "banana" ,"coconut"]
#           0         1           2          3
#print(fruits[4]) will be a index out of range error

# can in iterated in loops
for fruit in fruits:
    print(fruit)
# list methods
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

