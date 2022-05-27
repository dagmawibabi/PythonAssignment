
def guthrieSequence(number):
    n = number
    while n != 1:
        # Check if Even or Odd
        if n % 2 == 0:
            n = n / 2;
        else:
            n = (n * 3) + 1
        print (n);

guthrieSequence(7)