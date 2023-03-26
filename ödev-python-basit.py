# Proje-1

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l1 = []
def flatten(n):
    for i in n :
        if isinstance(i,list):
            flatten(i)
        else:
            l1.append(i)

flatten(l)
print(l1)

# Proje-2

sayılar = [[1, 2], [3, 4], [5, 6, 7]]
sayılar.reverse()
for i in range(len(sayılar)):
    (sayılar[i])=(sayılar[i])[::-1]

print(sayılar)