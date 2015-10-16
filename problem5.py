dict = {2501:False}

for n in range(2520, 999999999, 19):
    if dict[n-19] == False:
        dict[n] = True
        for i in range(1, 21):
            if dict[n] % i != 0:
                dict[n] = False
    else:
        print(dict[n-1])
        break
    print(n, dict[n])