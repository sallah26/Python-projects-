# # name = input("Hello please Enter your name: ")
# # print(f"Hello {name}!")
# age = int(input("Enter your age: "))
# if age > 18:
#     print('Account has been succesfully created!')
# else:
#     print ('Sorry, you are not eligable to use this system')

# arr = [int(i) for i in input().split(" ")[:3]]
# a = arr[0]
# b = arr[1]
# c = arr[2]
# if(a+b == c):
#     print("correct!")
# else:
#     print("wrong!")



# line = input()
# a, b = line.split()
# a = int(a)
# b = int(b)
# print(a + b)

# new_nums = []
# for i in numbers:
#     add = i + 1
#     new_nums.append(add)

# print("The squared numbers are ",new_numss)
# def evens(m):
#     loc = False
#     if m%2 == 0:
#         loc = True
#     return loc
# numbers = [1, 2, 3, 4, 5, 6]
# evenss = [i for i in numbers if i%2 != 0]
# # print()
# print("Even numbers are ",evenss)

# import csv
# arr = []
# with open("file1.txt") as File:
#     data = read(File)
#     print(data)
    # for row in data:
    #     print(row)
    #     arr.append(row[1])
    # print(arr)
        # for i in row:
        #     print(i)
with open("file1.txt", mode="r") as File:
    arr = File.readlines()
    # print(contents)
    # arr = contents.split()
    # arr = int(arr)
    # arr.remove()
    # print(arr)

with open("file2.txt", mode="r") as File2:
    arr2 = File2.readlines()
    # print(contentss)
    # arr2 = contentss.split()
    # arr = int(arr)
    # arr.remove()
    # print(arr2)
# arr = [int(l) for l in arr]
# arr2 = [int(m) for m in arr2]
# print(arr,"/n",arr2)
# commons = []
# for i in arr:
#     for j in arr2:
#         if  i == j:
#             commons.append(i)
# print(commons)
# comms = [int(co) for co in arr if co in arr2]
# print(comms)