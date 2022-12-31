def hanoi_cw(n, source, destination, spare):
  if n == 1:
    print("Move disk 1 from %s to %s" % (source, destination))
  else:
    # The following part is wrong (not using clockwise movements)!
    hanoi_cw(n-1, source, destination, spare)
    hanoi_cw(n-1, destination, spare, source)
    print("Move disk %d from %s to %s" % (n, source, destination))
    hanoi_cw(n-1, spare, source, destination)
    hanoi_cw(n-1, source, destination, spare)

if __name__ == "__main__":
    while 1:
        numOfTray = int(input("원반의 개수를 입력하세요!(종료 : 0) :"))
        if numOfTray == 0:
            break
        hanoi_cw(numOfTray, 'A', 'B', 'C')
