# Student ID : 10959684
# Gideon Bekoe
primeNum = []

number=int(input("Enter Number: "))
def isPrime(k):
    i = 2
    while (i < k):
        if k % i == 0:
            return False
        i = i + 1
    return True


def printNum(l):
    x= 2
    while x <= l:
        if isPrime(a):
            primeNum.append(x)
        x= x + 1


printNum(number)

numOfPrime = len(primeNum)
sum = 0

v = 0
while v< numOfPrime:
    sum += primeNum[v]
    v = v + 1

ans = sum / numOfPrime

print(ans)
