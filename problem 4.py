# Problem 4 
arr = []
i = 999
o = 999
num = 0 

while True:
    while True:
        num = i*o
        if str(num) == str(num)[::-1]:
            arr.append(num)
            break
        if i == 800:
            break
        i=i-1
    o -=1 
    i = 999
    if o == 800:
        break
print(max(arr))