
if __name__ =  '__main__':
    print("hello world")
    for n in range(3 , 15):
        a = [i * 0 for i in range(n + 1)]
        a[1] = 0
        for i in range(2, n + 1):
            a[i] = a[i - 1] + a[i - 2]
        print(a[i + 1])