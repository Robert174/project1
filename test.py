def ss(a, b):
    s = a + b
    return s

def sss(a, v):
    d = a * v
    print(d)

a = int(input())
b = a + 10
s = ss(a, b)
s1 = sss(s, b)
s2 = s + s1
print(s2)

