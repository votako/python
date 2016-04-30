f = [open('s.txt').read()]
b = []
for i in f[::-1]:
    b.append(f)
    print(b)
