numberOfCodes, mainCode = input().split()
numberOfCodes = int(numberOfCodes)

mainCodeSet = set(mainCode)

for i in range(numberOfCodes):
    code = input()
    if set(code) == mainCodeSet:
        print('Yes')
    else:
        print('No')
