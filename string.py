#in python  a string is a sequence of charachter. we can create string by enclosing charateter in quotes
  #Her single quotes is equal to double quotes
#opertion                                       synatx
#string length                                print(len(string_name))
#locate a character in string_name          print(string_name,index("char"))
#print a part of string                      print(string_name[start:stop])
#reverse a string                           print(string_name[::-1])
#convert a string to uppercasee             print(string_name.upper()) 
#convert a string to lowercasee             print(string_name.lower())
#count the number of time a character       print(string_count("char"))
#is repeated in a string


#print a string 
bun= "welcome to new fucking world"
print (bun)
#string lenth
print(len(bun))
#locate a character in a string
print(bun.index("l"))
#locate a count the number of time a character is  repeated in a string
print(bun.count("character specify"))
#print a part of string
print(bun[0:3])
#reverse a string
print(bun[::-1])
#convert a string to uppercasee 
print(bun.upper())
#concatenate a string
print(bun + "sample example")
#print a multiple times
print(bun * 12)
