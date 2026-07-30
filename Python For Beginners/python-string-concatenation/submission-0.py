def concatenate(s1: str, s2: str) -> str:
    joined = s1 + s2
    if len(joined) > 10:
        return "Too long!"
    else:
        return joined




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
