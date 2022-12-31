#
# A few operations on the BST
#

# Select here which implementation you want to use:
# Old one:
import bst
# New one
#import nrbst as bst

d = bst.dict()

d[7] = "ITM421"
d[3] = "ITM411"

print("d = %s" % d)
print("d[3] = %s" % d[3])
print("d[7] = %s" % d[7])

d[7] = "ITM421A"

print("d = %s" % d)
print("d[3] = %s" % d[3])
print("d[7] = %s" % d[7])

d[13] = "ITM511"
d[29] = "ITM613"

print("d = %s" % d)

del d[13]

print("d = %s" % d)

d[5] = "ITM414"
d[19] = "ITM423"
d[17] = "ITM426"
d[11] = "ITM416"

print("d = %s" % d)

del d[17]

print("d = %s" % d)

print("First key is %s" % d.firstkey())
print("Last key is %s" % d.lastkey())

print("Now testing an unbalanced insertion order:")
e = bst.dict()
n = 1010
for i in range(1, n):
    e[i] = str(i)

print("First key is %s" % e.firstkey())
print("Last key is %s" % e.lastkey())

del e[n // 2]

