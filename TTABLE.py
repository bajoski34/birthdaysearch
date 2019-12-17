count = 0

for i in range(1, 12+1):
    for k in range(1, 12+1):
        print(f"{i} x {k} = {i*k}")
        count = count + 1
        if count == 12:
            print("\n \t")
            count = 0
