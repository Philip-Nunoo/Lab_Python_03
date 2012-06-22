#Philip Afful Nunoo
print "Philip Afful Nunoo"

print "The first 50 prime numbers are"
#n = int(input("Enter number :"))
next1 = 0
count = 0
i = 1
while (i>0):
    cnt = 0
    for j in range(1,i+1,1):
        if (i%j == 0):
            cnt += 1
    if (cnt == 2):
        count +=1
        next1 += 1
        print i,
    if (count == 50):
        break
    if (next1 == 10):
        next1 = 0
        print ""
    i += 1
