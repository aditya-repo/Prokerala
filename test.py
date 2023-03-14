f = open("completedData.txt", "r")
arrays = ['abohar-jodhpur-express-14628.html','abu-road-mahesana-demu-special-13006.html']
delList = f.read()
f.close()
y = delList.split(",")
while("" in y):
    y.remove("")

print(len(y))
for each in y:
	arrays.remove(each)

print(arrays)




