
s = "/usr/local/bin/python.exe"

print(s[1:].replace("/",","))
print(s[0:11].replace("/","\\")+s[11:].replace("/",","))

