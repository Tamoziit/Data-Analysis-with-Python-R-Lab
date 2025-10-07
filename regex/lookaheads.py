import re

def min_window(s1, s2):
    pattern = ''.join(f'(?=.*{c})' for c in s2) + '.*'
    min_substr = None
    
    for i in range(len(s1)):
        for j in range(i + len(s2), len(s1) + 1):
            sub = s1[i:j]
            
            if re.match(pattern, sub):
                if min_substr is None or len(sub) < len(min_substr):
                    min_substr = sub
                    
    return min_substr

res = min_window("PRWSOERIUSFK", "OSU")
print(res)

"""
for s2 = "OSU" pattern becomes:
(?=.*O)(?=.*S)(?=.*U).* --> ie. from current position:
1. Look ahead (?=)
2. To find any character (.)
3. Such characters Maybe 0 or more (*)
4. followed by "O"/"S"/"U"
5. Lookaheads specify that O, S & U are searched independently (i.e., not in any order)
6. matches things like --> TGFH"O"hhdj"U"hhs"S"ghh --> looking ahead from "T" (?=) after "TGFH" (.*) we get "O" and so on
7. last .* specifies O, S, U patterns may have suffix of any character 0 or more times.
"""