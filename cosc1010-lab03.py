# Marek Amraly
# UWYO COSC 1010
# 9/26/24
# Lab 03 
# Lab Section: 
# Sources, people worked with, help given to: 
# your
# comments
# here



# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list

l1 = [
    "Wyoming",
    "Colorado",
    "Montana"
]

print(l1)

#print the entire list


#now print the first element in the list

print(l1[0])
#Print the last element using the syntax shown in class to access the final element (hint, think negatives)

print(l1[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided

print(f"{l1[1].upper()} is south of {l1[0].upper()}")

print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list

l1.extend(["Washington", "Oregon", "California"])
print(l1)
#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 

l1[-2] = 'Maine'

print(l1)

#Insert the state Texas to be the third element in the list, again printing your list

l1.insert(2, "Texas")
print(l1)

#Using the `del` statement remove the fourth item from the list, print your list 

l1.__delitem__(3)
print(l1)

#Remove Texas using its value, print the list

l1.remove('Texas')
print(l1)

print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 

print(l1.sort())
print(l1)

#Permanently sort your list in reverse order, printing it out

l1.sort(reverse=True)
print(l1)

#Using the reverse method reverse the list and print it

l1.reverse()
print(l1)