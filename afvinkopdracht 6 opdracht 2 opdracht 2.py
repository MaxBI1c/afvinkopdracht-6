def main():
    total = 0.0
    
    numbers = open('numbers.txt','r')
    for line in numbers:
        amount = float(line)
        total += amount

    numbers.close()
    print(total)
main()
