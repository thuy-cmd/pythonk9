import string
name = "hoang van bit"
print(name.title())

a = name.split()
result = ''
for txt in a:
    result += txt[0].upper() + txt[1:] + " "
print(result)

print(string.capwords(name))