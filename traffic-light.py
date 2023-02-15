test = int(input())

for _ in range(test):
    n, currPos = input().split()
    string = input()
    string = string + string
    
    maxi= 0
    
    for i,light in enumerate(string):
        if light == currPos:
            j = i
            while j < len(string) and string[j] != "g" :
                j+=1
            maxi = max(maxi, j-i)
    print(maxi)
            
            
    

