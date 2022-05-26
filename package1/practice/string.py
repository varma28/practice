
str1 = input()
str2 = ''


for i in range(0,len(str1)):
    
    if(i%2 == 0 and str1[i].islower):
        
        str1 += str1[i].swapcase()
    elif(i%2 != 0):
        str1 += str1[i]
    


print(str1)

