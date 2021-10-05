#1
# try:
#     print("Hello")
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")
#


#2
# try:
#     print(x)
# except:
#     print("Something went wrong")
# finally:
#     print("The 'try except' is finished")


#3
# try:
#     f = open("demofile.txt")
#     try:
#         f.write("Lorum Ipsum")
#     except:
#         print("Something went wrong when writing to the file")
#     finally:
#         f.close()
# except:
#     print("Something went wrong when opening the file")


#4
# x = -1
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

#5
x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")