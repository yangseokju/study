num = 1
a = int(input())

while a>0:
    b = list(map(int,input().split()))
    avg = sum(b)/len(b)
    print("#{0}".format(num),"%d"%avg)
    a -= 1
    num += 1