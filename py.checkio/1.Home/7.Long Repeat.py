"""
This mission is the first one of the series. Here you should find the length of 
the longest substring that consists of the same letter. For example, line 
"aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and 
"aaaa". The last substring is the longest one which makes it an answer.

Input: String.
Output: Int.
"""

def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    count = 0
    letter = []
    for i in line:
        if i in letter or len(letter) == 0:
            letter.append(i)
            count = len(letter) if len(letter) > count else count
        else:
            letter = [i]
    # your code here
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
