#
# Execute some set operations
#

from ibst import Set
#from solution import Set

a = Set()
for el in [13, 9, 2, 99, 12, 88, 55, 57]:
  a = a + el

print("a = %s" % a)

b = a + 50

print("After b = a + 50, we have")
print("a = %s" % a)
print("b = %s" % b)

c = a - 13

print("After c = a + 13, we have")
print("a = %s" % a)
print("b = %s" % b)
print("c = %s" % c)

print("a.upper_neighbor(2) = %d" % a.upper_neighbor(2))
print("c.upper_neighbor(12) = %d" % c.upper_neighbor(12))
print("c.upper_neighbor(0) = %d" % c.upper_neighbor(0))
print("c.upper_neighbor(50) = %d" % c.upper_neighbor(50))
print("c.upper_neighbor(55) = %d" % c.upper_neighbor(55))
try:
    print("c.upper_neighbor(99) = %d" % c.upper_neighbor(99))
except KeyError as e:
    print("c.upper_neighbor(99): KeyError(%s)" % e)

print("a.range(-10, 10) = %s" % a.range(-10, 10))
print("a.range(12, 57) = %s" % a.range(12, 57))
print("a.range(57, 105) = %s" % a.range(57, 105))
print("a.range(100, 105) = %s" % a.range(100, 105))
print("c.range(56, 80) = %s" % a.range(56, 80))

a1, a2 = a.split(40)
print("After a1, a2 = a.split(40) we have:")
print("a = %s" % a)
print("a1 = %s" % a1)
print("a2 = %s" % a2)

a1, a2 = a.split(3)
print("After a1, a2 = a.split(3) we have:")
print("a = %s" % a)
print("a1 = %s" % a1)
print("a2 = %s" % a2)

a1, a2 = a.split(99)
print("After a1, a2 = a.split(99) we have:")
print("a = %s" % a)
print("a1 = %s" % a1)
print("a2 = %s" % a2)

