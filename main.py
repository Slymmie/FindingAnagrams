# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(str1, str2):
    if(sorted(str1)== sorted(str2)):  
        return True 
    else:  
        return False 
str1 = "comrade"
str2 = "compare"
print(find_anagram(str1,str2))
str1 = "orobo"
str2 = "brooo"
print(find_anagram(str1,str2))
