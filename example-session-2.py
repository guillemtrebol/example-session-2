var1 = input("Enter something: ")

print("Output: {}".format(var1))

var2 = ""
for i in range(len(var1) - 1, -1, -1):
    var2 += var1[i]
print("Output: {}".format(var2))

var3 = 0
for letter in var1:
    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        var3 += 1
print("Output: {}".format(var3))

var4 = ""
for i in range(len(var1)):
    if i % 2 == 0:
        var4 += var1[i].upper()
    else:
        var4 += var1[i].lower()
print("Output: {}".format(var4))

var5 = ""
for letter in var1:
    if letter != " ":
        var5 += letter
print("Output: {}".format(var5))
