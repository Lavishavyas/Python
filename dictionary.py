d = {100 : "abc", 102 : "xyz", 105 : "pqr"}
print(d)

d = {}
d["laptop"] = 40000
d["mobile"] = 15000
d["earphones"] = 1000
print(d)
print(d["mobile"])

d = {100 : "abc", 102 : "xyz", 105 : "pqr"}
print(d.get(101))
print(d.get(125))
print(d.get(125, "NA"))
if 125 in d:
    print(d[125])
else:
    print("NA")


d = {100 : "abc", 102 : "xyz", 105 : "pqr", 106 : "bcd"}
d[101] = "wxy"
print(len(d))
print(d)
print(d.pop(105))
print(d)
del d[106]
print(d)
d[108] = "cde"
print(d.popitem())










































# ✅ Definition of Dictionary in Python:
# A dictionary in Python is a mutable, unordered collection of items where each item is stored as a key-value pair.

# It allows fast access, addition, and deletion of data based on unique keys.

# 🧠 Key Points:
# Mutable: Can be changed after creation.

# Unordered (as of Python < 3.7): No guaranteed order of items.

# Key-value pair: Each key maps to a specific value.

# Keys must be unique and immutable (e.g., strings, numbers, tuples).

# Values can be any data type.

