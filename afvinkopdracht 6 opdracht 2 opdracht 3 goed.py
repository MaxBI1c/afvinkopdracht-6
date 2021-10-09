def main():
    hallo = open('woorden.txt','w')
    
    wrd1 = input('Voer een woord in')
    wrd2 = input('Voer een woord in')
    wrd3 = input('Voer een woord in')
    wrd4 = input('Voer een woord in')
    wrd5 = input('Voer een woord in')

    hallo.write(wrd1 + '\n')
    hallo.write(wrd2 + '\n')
    hallo.write(wrd3 + '\n')
    hallo.write(wrd4 + '\n')
    hallo.write(wrd5 + '\n')

    hallo.close()
    print('Woorden geschreven naar woorden.txt')
    
main()
