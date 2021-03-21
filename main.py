import json

from pip._vendor.urllib3.connectionpool import xrange

obj = json.load(open("venv/JsonFiles/semt.json"))

ilk_durum = len(obj)

my_list = []
# Iterate through the objects in JSON and pop (remove)
# the object once we find it

number = 0

for i in xrange(len(obj)):
    if obj[i]["SEMT_ADI"] == "Köyler":
        my_list.append(i)
        print(i)
        number = number + 1

fark = number

print(number)

for x in xrange(len(my_list)):
    obj.pop(x)
    number = number - 1

print(number)

print(len(obj))

# Output the updated file with pretty JSON
open("venv/JsonFiles/updated-semt.json", "w").write(
    json.dumps(obj, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': '))
)

yeniObj = json.load(open("venv/JsonFiles/updated-semt.json"))

son_durum = len(yeniObj)

if( ilk_durum - son_durum == fark ):
    print("true")



