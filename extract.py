a = [1,4,9,16, 25, 36, 49, 64,81,100]
# even = []
# for n in a:
#     if n % 2 == 0:
#         even.append(n)
# print(even)   

res = list(filter(lambda x: x % 2 == 0, a))
print(res)


