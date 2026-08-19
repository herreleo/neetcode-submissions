class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_keys = []

        anagrams_list = {}
        anagram = []
        anagram_set = set()
        #first loop and scramble list 
        for words in strs:
            #make each string into list
            #then sort and join this list 
            char_list = []
            for char in words:
                char_list.append(char)
            char_list.sort()
            result = ''.join(char_list)
            sorted_keys.append(result)

        # print(sorted_keys)
        # print(strs)

        for key in sorted_keys:
            anagram_set.add(key)
        
        keys = []
        for key in anagram_set:
            keys.append(key)


        for key in keys:
            anagrams_list[key] = []
        
        for words in strs:
            char_list = []
            result_word = ""
            for char in words:
                char_list.append(char)
            char_list.sort()
            result_word = ''.join(char_list)

            anagrams_list[result_word].append(words)
        

        for key in anagrams_list:
            value = anagrams_list[key]
            anagram.append(value)

    
        return anagram