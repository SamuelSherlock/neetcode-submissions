from typing import List

def read_integers() -> List[int]:
    int_list = [int(x) for x in input().split(",")]
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
