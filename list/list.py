lst = [1,2,3,4,5]
lsted = sorted(lst, reverse=True)
print(lsted) 
print("*"*35)
lst.sort(reverse=True)
print(lst)
print("*"*35)
print(' '.join(str(x) for x in lst[::-1]))
print("*"*35)