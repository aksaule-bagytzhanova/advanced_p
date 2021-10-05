#syntax

'''


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")

'''

'''
except (RuntimeError, TypeError, NameError):
    pass

'''


import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())

except OSError as err:
    print("OS error: {0}".format(err))

except ValueError:
    print("Could not convert data to an integer. ")
except:
    print("Unexpected error: ", sys.exc_info()[0])
    raise

