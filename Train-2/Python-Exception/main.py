a = 5
b = 0


# print(a/b)

# try:
#     print(a/b)
# except:
#     print("Invalid expression")


arr = [1,2,3,4,2,12,32]
 
try:
    print(arr[10])
    print(a/b)
except IndexError:
    print("Invalid index error")
except ZeroDivisionError:
    print("Invalid to divide number by zero")