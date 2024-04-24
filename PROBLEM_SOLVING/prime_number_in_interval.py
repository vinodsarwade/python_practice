lower_intervel  = int(input("enter a lower number  from where to start prime numbers: "))
upper_intervel  = int(input("enter a upper number up to where to ends prime numbers: "))

if lower_intervel and upper_intervel <= 1:
    print("neither prime nor composite number")

if lower_intervel and upper_intervel > 1:
    for num in range(lower_intervel, upper_intervel):
        for j in range(2, num):

            if num % j == 0:
                print(f"{num} not a prime number")
                break
        else:
            print(f"{num} prime number")