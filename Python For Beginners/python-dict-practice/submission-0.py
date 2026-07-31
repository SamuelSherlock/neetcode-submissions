from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count_dict = {}
    for i in word:
        count = 0
        for j in word:
            if i == j:
                count += 1
        count_dict[i] = count
    return count_dict
        




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
