t = (10, 20, "geek")
print(t)
t = ()
print(type(t))
t = 10
print(type(t))
t = (10,)
print(type(t))

t = 10, 20, 30, 40, 10
print(t[2])
print(t[-1])
print(t[1:3])
print(len[t])
print(t.count(10))
print(t.index(20))


# ✅ Definition:
# A tuple is a built-in data structure in Python used to store an ordered collection of elements. Unlike lists, tuples are immutable, meaning their contents cannot be changed after creation.

# 🔹 Key Characteristics:
# Ordered: Elements are stored in a defined sequence.

# Immutable: Cannot be modified after creation.

# Heterogeneous: Can contain elements of different data types.

# Allows Duplicates: Elements can be repeated.

# Hashable: Tuples can be used as keys in dictionaries (if all elements are also hashable).

