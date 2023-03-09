string= "HELooEdYoDa"

def upper_lower(str):
    lower=0
    upper=0
    for i in str:
        if(i.islower()):
            lower+=1
        else:
            upper+=1
    return lower,upper 

lower,upper=upper_lower(string)    
print(lower,upper)   

##output: 5 6

