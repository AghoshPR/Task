import re

def regexfind(P):
    
    
    regex_integer_in_range=r"^[1-9][0-9]{5}"
    regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"
    
    if (bool(re.match(regex_integer_in_range,P)) and len(re.findall(regex_alternating_repetitive_digit_pair,P))<2 ):
        
        return 'Valid'
    return 'Invalid'
    

print(regexfind('110000'))
