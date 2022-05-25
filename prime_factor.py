def prime_factor(n):
    i = 2
    while(n>1):
        while(n%i == 0):
            print(i)
            n = n//i
        i = i+1

def main():
    n = int(input('Enter a number'))
    prime_factor(n)

if __name__ == '__main__':
    main()

    