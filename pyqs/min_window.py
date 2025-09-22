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
print("Min. Window =", res)