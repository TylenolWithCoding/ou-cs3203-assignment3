def adder(list):
    sum = 0
    for i in list:
        sum += i
    
    return sum

def producter(list):
    sum = 1
    for i in list:
        sum = sum * i
    
    return sum

def reverser(list):
    d = []
    for i in reversed(list):
        d.append(i)

    return d
//tivial change for part 10
def main():
    b = []
    size = int(input("How many numbers are you providing? "))

    for i in range(0, size):
        c = int(input("Enter your number and press enter after each one: "))
        b.append(c)

    print(adder(b))
    print(producter(b))
    print(reverser(b))
if __name__ == "__main__":
    main()

