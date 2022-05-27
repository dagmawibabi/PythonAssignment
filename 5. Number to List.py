num = 2019
def numberToList(number):    
    print ("The original number is " + str(num))
    result = [int(x) for x in str(num)]
    print ("The list from number is " + str(result))

numberToList(num)

