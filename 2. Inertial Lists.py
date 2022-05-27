from multiprocessing.spawn import is_forking


def hasOdd(list):
    isOdd = False
    oddCount = 0
    for x in list:
        if x % 2 != 0:
            isOdd = True
        if isOdd == True:
            oddCount += 1
            isOdd = False    
    if oddCount > 0:
        return True
    else:
        return False   

def isMaxEven(list):
    maxNum = max(list)
    if maxNum % 2 == 0:
        return True
    else:
        return False 

def isEveryOddGreater(workingList):
    even = []
    odd = []
    everyOddGreater = []
    # remove max even
    list = workingList
    maxNum = max(list)
    while maxNum in list:
        list.remove(maxNum)
    # Separate the even and odd
    for x in list:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    # Compare
    for x in odd:
        for y in even:
            if x > y:
                everyOddGreater.append(True)
            else:
                everyOddGreater.append(False)
    # Return result
    if False in everyOddGreater:
        return False
    else:
        return True

def isInertialList(list):
    if hasOdd(list) == True:
        if isMaxEven(list) == True:
            if isEveryOddGreater(list) == True:
                print(list, " is Inertial List")
                return 1
            else:
                print(list, " is not Inertial List. Every odd is not greater than the even.")
                return 0
        else:
            print(list, " is not Inertial List. The max value is not even.")
            return 0
    else:
        print(list, " is not Inertial List. List doesn't contain odd numbers.")
        return 0

sampleList = [1,2,3,4]
sampleList2 = [2, 12, 12, 4, 6, 8, 11]

print(isInertialList(sampleList2))