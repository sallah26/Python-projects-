import csv
import pandas
# arr = []
# with open("weather_data.csv") as File:
#     data = csv.reader(File)
#     print(data)
#     for row in data:
#         print(row)
#         arr.append(row[1])
#     print(arr)
#         # for i in row:
#         #     print(i)
# # arr2 = arr[1:]
# arr2 = [int(inp) for inp in arr[1:]]
# print(arr2.max())

# import webbrowser
# webbrowser.open("www.canva.com")
#     data = csv.reader(File)
#     for i in data:
#         arr.append(i[1])
# print(data)
# print(f"The Temprature of this week are: {arr2}")
# data_html = data.to_html()
# data_html = data.to_clipboard()
# data_html = data.to_html()
# sum = 0
# for i in data_list:
#     sum+=i
# print(f"The average is {sum/len(data_list)}")
# print(data_html)u
# print(ddata[1])

##Accessing 

# data = pandas.read_csv("Squirrel_Data.csv")
# # print(data)
# data_list = data["Primary Fur Color"].tolist()
# Gray = data_list.count("Gray")
# Cinnamon = data_list.count("Cinnamon")
# Black = data_list.count("Black")
# # print(data_list)
# print(f"Black = {Black}, gray = {Gray}, Cinnamon = {Cinnamon}")

data = pandas.read_csv("./weather_data.csv")

mon_data = data[data.day == "Monday"]
print(mon_data.temp)
mtemp = mon_data.temp
print(int(mtemp))


# ddict = {
#     "Colors" : ["Gray", "Cinnamon", "Black"],
#     "Amount" : [Gray, Cinnamon, Black]
# }
# df = pandas.DataFrame(ddict)
# df.to_csv("Amount-of-colors.csv")
# print(ddict)
# colorss = pandas.read_csv("Amount-of-colors.csv")
# print(colorss)