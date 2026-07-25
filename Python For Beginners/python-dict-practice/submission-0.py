from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    character_count = {}

    for char in word:
        if char in character_count:
            character_count[char] +=1
        
        else:
            character_count[char] = 1

    return character_count
            
    #I loop through the word 
    #for each char I check if in dictonary, if not add and value to one, 
    #if exisit in dictoantyy cahnge value 



# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
