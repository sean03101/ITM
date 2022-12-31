
#from doublylinkedlist import DoublyLinkedList
from solution import DoublyLinkedList

def make(*els):
  a = DoublyLinkedList()
  for e in els:
    a.append(e)
  return a

def check(name, a, ref):
  correct = "Correct" if str(a) == ref else "INCORRECT!!"
  print("%s = %s %s" % (name, str(a), correct))

def checkNode(text, n, ref):
  correct = "Correct" if n == ref else "INCORRECT!!"
  print("%s = %s %s" % (text, str(n), correct))

a = make(1, 3, 5, 7, 9, 11, 3, 9, 3, 11, 7, 11, 13, 5)
check("a", a, "[1, 3, 5, 7, 9, 11, 3, 9, 3, 11, 7, 11, 13, 5]")

checkNode("a.find_first(3)", a.find_first(3), a.first().next)
checkNode("a.find_first(9)", a.find_first(9), a.first().next.next.next.next)
checkNode("a.find_last(3)", a.find_last(3), 
          a.first().next.next.next.next.next.next.next.next)
checkNode("a.find_last(11)", a.find_last(11), a.last().prev.prev)
checkNode("a.find_first(27)", a.find_first(27), None)
checkNode("a.find_last(81)", a.find_last(81), None)

b = DoublyLinkedList()
check("b", b, "[]")
checkNode("b.find_first(3)", b.find_first(3), None)
checkNode("b.find_last(3)", b.find_last(3), None)

print("a.count(3) = %d" % a.count(3))
print("a.count(11) = %d" % a.count(11))
print("a.count(7) = %d" % a.count(7))
print("a.count(37) = %d" % a.count(37))

a.remove_first(3)
print("After a.remove_first(3)")
check("a", a, "[1, 5, 7, 9, 11, 3, 9, 3, 11, 7, 11, 13, 5]")

a.remove_first(11)
print("After a.remove_first(11)")
check("a", a, "[1, 5, 7, 9, 3, 9, 3, 11, 7, 11, 13, 5]")

a.remove_first(-12)
print("After a.remove_first(-12)")
check("a", a, "[1, 5, 7, 9, 3, 9, 3, 11, 7, 11, 13, 5]")

a.remove_last(11)
print("After a.remove_last(11)")
check("a", a, "[1, 5, 7, 9, 3, 9, 3, 11, 7, 13, 5]")

a.remove_last(81)
print("After a.remove_last(81)")
check("a", a, "[1, 5, 7, 9, 3, 9, 3, 11, 7, 13, 5]")

b.remove_first(81)
print("After b.remove_first(81)")
check("b", b, "[]")

b.remove_last(81)
print("After b.remove_last(81)")
check("b", b, "[]")

a = make(1, 3, 5, 7, 9, 11, 3, 9, 3, 11, 7, 11, 13, 5)
print("a = %s" % a)
a.remove_all(11)
print("After a.remove_all(11)")
check("a", a, "[1, 3, 5, 7, 9, 3, 9, 3, 7, 13, 5]")
a.remove_all(37)
print("After a.remove_all(37)")
check("a", a, "[1, 3, 5, 7, 9, 3, 9, 3, 7, 13, 5]")
a.remove_all(3)
print("After a.remove_all(3)")
check("a", a, "[1, 5, 7, 9, 9, 7, 13, 5]")

b.remove_all(81)
print("After b.remove_all(81)")
check("b", b, "[]")

a = make(1, 3, 5, 7, 9, 11, 3, 9, 3, 11, 7, 11, 13, 5)
print("a = %s" % a)
n = a.find_first(5)
m = a.find_last(9)
b = a.takeout(n, m)
print("After b = a.takeout(n, m)")
check("a", a, "[1, 3, 3, 11, 7, 11, 13, 5]")
check("b", b, "[5, 7, 9, 11, 3, 9]")

c = b.takeout(b.first(), b.last())
print("After c = b.takeout(b.first(), b.last())")
check("b", b, "[]")
check("c", c, "[5, 7, 9, 11, 3, 9]")

d = c.takeout(c.first().next, c.find_first(11))
print("After d = c.takeout(c.first().next, c.find_first(11))")
check("c", c, "[5, 3, 9]")
check("d", d, "[7, 9, 11]")
