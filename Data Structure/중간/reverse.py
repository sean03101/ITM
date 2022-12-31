# Reverse input string

from liststack import Stack

def reverse(s):
  S = Stack()
  for ch in s:
    S.push(ch)
  while not S.is_empty():
    ch = S.pop()
    print(ch, end="")
  print()

if __name__ == "__main__":
  while True:
    s = input("Enter a string> ")
    if s is None or s.strip() == "":
      break
    reverse(s)


