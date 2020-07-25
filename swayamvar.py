n = int(input())

strb = (input())
strg = (input())
i = 0

while i < n:
    index = strg.find(strb[0])

    if index<0:
        break
    strg = strg[index+1:]+strg[:index]
    strb = strb[1:]
    i+=1
print(len(strb))
