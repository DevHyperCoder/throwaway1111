def prime(n):
    if n == 1:
        print("1 is neither composite nor prime.")
        return

    for i in range(2,n):
        if n % i == 0:
            print(n, "is not prime.")
            break
    else:
        print(n,"is prime.")

num = int(input("Enter a number: "))
prime(num)
