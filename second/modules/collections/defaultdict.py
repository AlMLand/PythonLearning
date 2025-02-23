from collections import defaultdict

d = {"a": 10}
print(d)

###

dd = defaultdict(lambda: "default value when key is not present")
dd[1] = "some value"

print(dd[44])
print(dd[1])
