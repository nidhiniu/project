# 151. Reverse Words in a String
# Medium
# Topics
# Companies
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


class String_reverse:
    def reverseWords(self, s: str) :
        
        try:
            if not isinstance(s, str):
                raise ValueError("Input must be a string.")
            
            
            words = s.split()
            reversed_words = []
            
            for word in words:
                reversed_words.insert(0, word)  
            
            return " ".join(reversed_words)
        
        except ValueError as e:
            print(f"Error: {e}")
            return ""  

string_object = String_reverse()
result = string_object.reverseWords("India is going to lose this test agianst newzealand")
print(result) 


