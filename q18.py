s = """We encourage everyone to contribute to Python. If you still have questions
after reviewing the material
in this guide, then the Python Mentors group is available to help guide new
contributors through the process."""

list = s.upper().replace('\n', ' ').replace('.', '').replace(',', '').split(' ')
result = {}

for i in list:
    try:    result[i] += 1
    except: result[i] = 1
    print(i)
print("="*20)
sortedList = sorted(result.keys())

for i in sortedList:
    print(i,':',result[i])


