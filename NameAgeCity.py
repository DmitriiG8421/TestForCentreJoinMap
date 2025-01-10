columnsTitles = "Name   |   Age   |   City"
columns = ["name", "age", "city"]


x = list(map(lambda  a : input("Please type your "+ a +": "),columns))

print(columnsTitles.center(len(columnsTitles)+25,"-"))
print("   |   ".join(x).center(len(columnsTitles)+25,"-"))